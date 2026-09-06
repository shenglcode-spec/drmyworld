# Java高级 JVM调优、并发编程、字节码

## 面试要点

### JVM 调优
- 理解 JVM 内存结构：堆（Young/Old）、方法区（Metaspace）、栈、本地内存（Native）和直接内存（Direct ByteBuffer）。
- 常见 GC 算法与实现：Serial, Parallel, CMS, G1, ZGC, Shenandoah；了解各自优缺点和适用场景。
- 关键 JVM 启动参数：-Xms/-Xmx/-Xmn、-Xss、-XX:MetaspaceSize、-XX:+UseG1GC、-XX:MaxGCPauseMillis 等。
- GC 日志与诊断：会开启并分析 GC 日志（-Xlog:gc* 或 -XX:+PrintGCDetails），判断 Minor/Full GC、内存泄漏与 OOM 的区别。
- JIT 编译与性能：理解热点编译、内联、逃逸分析（escape analysis）、方法消除等优化对性能的影响。
- ClassLoader 与类加载机制：双亲委派、热部署和类卸载的基本原理。
- 性能调优工具：jstat、jmap、jstack、jcmd、jinfo、jvisualvm、Java Flight Recorder (JFR)、async-profiler。

### 并发编程
- Java 内存模型（JMM）和 happens-before 原则，volatile、synchronized 与 final 的语义和用途。
- 线程基础与线程池：Thread、Runnable、Callable、Future，线程池参数（核心线程数、最大线程数、队列、拒绝策略）。
- 锁与无锁：偏向锁/轻量级/重量级锁、CAS 操作、Atomic 类、ReentrantLock、ReadWriteLock、StampedLock。
- 并发集合与并发工具类：ConcurrentHashMap、ConcurrentLinkedQueue、BlockingQueue、CountDownLatch、CyclicBarrier、Semaphore、Exchanger。
- 常见并发问题：死锁、活锁、饥饿、ABA 问题，诊断与解决方法（锁顺序、定时等待、检测、断言）。
- 并发模式与异步编程：生产者-消费者、线程池模型、ForkJoin 框架、CompletableFuture、Reactive 编程基础。

### 字节码 & 类加载
- 类加载流程：加载（Loading）、验证（Verification）、准备（Preparation）、解析（Resolution）、初始化（Initialization）；理解静态初始化与类初始化时机。
- 双亲委派模型与自定义 ClassLoader 的场景与风险。
- 字节码结构基础：Class 文件结构、常量池、方法区、局部变量表与操作数栈。
- 字节码工具与实践：javap 反编译、ASM/BCEL/ByteBuddy/javassist 等库用于字节码增强与生成。
- 反射、动态代理与性能：反射的开销、MethodHandle 与 invokedynamic 简介。
- Java 模块化与兼容性：字节码版本、跨版本兼容性、JPMS（Java Platform Module System）影响。

## 面试题（含参考要点）

### JVM 与性能相关
1. 说明 JVM 的内存结构（堆/栈/方法区/本地内存）。
   - 要点：堆用于对象分配；Young/Old 分代；栈保存局部变量和方法帧；方法区（Metaspace）保存类元数据；本地内存用于 JNI 等。

2. 常见的 GC 算法有哪些？分别适合什么场景？
   - 要点：Serial（单线程，适用于客户端）；Parallel（吞吐量优先）；CMS（低停顿，老年代并发收集，易碎片）；G1（面向大堆、可预测停顿）；ZGC/Shenandoah（超低停顿，适合超大堆）。

3. 如何排查 Full GC 或频繁 GC？
   - 要点：查看 GC 日志、堆使用情况（jstat/jmap），分析对象创建/泄漏（jmap -histo），检查大对象、过小的堆或 Metaspace、过多的 Promotion 等。

4. -Xmx 与 -Xms 的区别及调优策略？
   - 要点：-Xms 初始堆，-Xmx 最大堆。生产上通常设置相同以避免扩缩容停顿；根据应用内存需求和 GC 行为调整 Young/Old 比例。

5. JIT 是如何工作的？逃逸分析是什么？
   - 要点：JIT 收集运行时热点并编译为本地代码；逃逸分析判断对象是否只在方法内使用，可能分配在栈上或被消除。

6. 描述一次常见的内存泄漏场景及如何定位。
   - 要点：静态集合、Listener 未注销、ThreadLocal 泄漏、缓存无限制增长。定位用 jmap/jhat/VisualVM/heap dump 分析，查大对象及其引用链。

### 并发与多线程
7. volatile 能否保证原子性？什么场景需要用 volatile？
   - 要点：volatile 保证可见性和禁止指令重排序，但不保证复合操作的原子性。适用于状态标志、双重检查锁定中的检查变量等场景。

8. synchronized 与 ReentrantLock 的区别及适用场景？
   - 要点：synchronized 是 JVM 内建的、语法级别的，自动释放锁；ReentrantLock 提供更多可控能力（公平锁、尝试加锁、可中断锁、条件变量）。

9. 解释 CAS（Compare-And-Swap）与 ABA 问题，如何解决 ABA 问题？
   - 要点：CAS 是无锁并发的基础；ABA 是值被改回导致误判，解决：使用版本号（AtomicStampedReference）或引入额外标识。

10. 说说线程池如何选择核心参数？RejectedExecutionHandler 常见策略有哪些？
    - 要点：根据任务特性（CPU 密集/IO 密集）、响应时间、吞吐量选 core/max/queue；拒绝策略：AbortPolicy（抛异常）、CallerRunsPolicy（回退到调用者执行）、DiscardPolicy（丢弃）、DiscardOldestPolicy（丢弃队列中最旧）。

11. 什么是 Happens-Before 关系？举例说明。
    - 要点：happens-before 定义操作之间的可见性/有序性保证。示例：释放锁的解锁操作 happens-before 随后获取相同锁的加锁操作；volatile 写 happens-before 随后读相同变量操作。

12. 如何避免死锁？如何定位死锁？
    - 要点：避免嵌套锁或规定统一加锁顺序；使用 tryLock 与超时；定位用 jstack 输出查看 BLOCKED/WAITING 状态和锁持有关系。

### 字节码与类加载
13. 描述类加载的五个阶段。什么时候会触发类的初始化？
    - 要点：加载、链接（验证/准备/解析）、初始化。初始化在首次主动使用类时触发（new、调用静态方法、读取静态字段等）。

14. 双亲委派模型是什么？为什么要有它？如何绕过？
    - 要点：类加载器向父加载器委托，保证核心类不会被自定义类覆盖，避免类重复加载。绕过：自定义 ClassLoader 并修改委派逻辑或直接用 findClass 加载。

15. 如何用 javap 查看编译后的字节码？举例说明一个简单方法的字节码包含哪些信息。
    - 要点：使用 javap -c ClassName；可看到局部变量表、操作数栈上的指令、invokevirtual/getfield 等指令。

16. 什么是 invokedynamic？有什么作用？
    - 要点：invokedynamic 是为动态语言和 lambda 优化引入的字节码指令，延迟解析调用点绑定，提高动态调用性能，支持 invokedynamic 引导方法（bootstrap method）。

17. 介绍常用字节码增强库及使用场景（ASM/ByteBuddy/javassist）。
    - 要点：ASM 轻量且灵活适合低级字节码操作；ByteBuddy 更高层次、更友好，常用于代理与 runtime 增强；javassist 基于源码风格的修改，易用。

### 综合/情景题
18. 线上发现频繁 Full GC，如何逐步定位与解决？（说出排查步骤）
    - 要点：收集 GC 日志与堆转存，查看 OOM 报错栈；使用 jstat/jmap/jcmd 检查各代占用，分析是否 Promotion failed、Metaspace OOM、JNI 内存等；根据结果调整堆/GC 策略、定位内存泄漏或优化对象生命周期。

19. 设计一个高并发下的缓存方案，保证读多写少且内存可控（谈数据结构/并发控制/过期策略）。
    - 要点：使用 ConcurrentHashMap + 值对象保存元信息，结合定时/惰性过期或 LRU/Size 限制（LinkedHashMap 或 Caffeine），考虑弱引用/软引用，采用写时复制或分段锁、设置合理的缓存清理策略。

20. 解释一下 CompletableFuture 的优势，并给出一个异步组合的示例场景。
    - 要点：更易链式组合、非阻塞回调、异常处理和线程池自定义；示例：并行调用多个远程服务，thenCombine 汇总结果，exceptionally 处理异常。

---

（可根据目标岗位侧重扩展每一节的深度：例如追求 JVM 专家岗可增加 GC 实现源码分析与调度器；追求中间件/框架岗可增加 ClassLoader 与字节码生成实践题）
