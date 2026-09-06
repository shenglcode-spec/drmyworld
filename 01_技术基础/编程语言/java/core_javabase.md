# Java核心基础、集合、JVM、并发

> 本文档补充了面试中常考的核心要点与若干实战案例，侧重知识点梳理、答题要点与工程实践思路，方便复习与面试准备。

## 目录
- 面试核心要点
  - Java 基础
  - 集合框架
  - JVM 与内存
  - 并发与多线程
- 常见面试题要点（示例）
- 实战案例与练习题（含解题要点）
- 面试题及答案

---

## 面试核心要点

### Java 基础
- Java 内存模型（JMM）基础：可见性、有序性、原子性；volatile 的作用与局限。
- 值语义与引用语义；基本类型与引用类型的区别。
- 类加载与初始化顺序（加载、连接、初始化）、双亲委派模型。
- 面向对象四大特性：封装、继承、多态、抽象。多态实现机制（虚方法表）。
- 异常处理：checked vs unchecked、异常链、finally 与 try-with-resources。
- 常见 API：String/Math/Optional/Stream 的常用用法与坑点（String 常量池、不可变性）。

### 集合框架
- Collection 与 Map 的体系结构与常见实现类（ArrayList, LinkedList, HashMap, LinkedHashMap, TreeMap, HashSet, ConcurrentHashMap 等）。
- HashMap 原理：hash、链表/红黑树转换、resize 触发条件与复杂度分析。
- ArrayList vs LinkedList 场景选择与复杂度（随机访问、插入/删除）。
- Iterator 与 fail-fast 机制（modCount）、如何安全地在迭代中修改集合。
- 等级别的并发集合选择：CopyOnWriteArrayList、ConcurrentHashMap、BlockingQueue 的使用场景。

### JVM 与内存
- JVM 内存区域：堆（年轻代/老年代）、方法区（或元空间）、栈、本地方法栈、直接内存。
- GC 基本算法：标记-清除、复制、标记-整理；分代收集思想与常见收集器（Serial, Parallel, CMS, G1 等）。
- OOM 常见类型与排查：Java 堆内存溢出（-Xmx）、方法区/Metaspace 溢出、StackOverflow、DirectBuffer 问题。
- 常用诊断工具：jmap、jstack、jstat、jcmd、VisualVM、async-profiler、GC 日志分析。
- 类加载器与内存泄漏：静态集合、线程池、监听器、ClassLoader 泄漏场景。

### 并发与多线程
- 线程创建方式、线程生命周期、线程池（ThreadPoolExecutor）参数理解与调优。
- synchronized、ReentrantLock、volatile、Atomic* 的语���与适用场景。
- 线程间协作：wait/notify、Condition、CountDownLatch、CyclicBarrier、Semaphore、Exchanger。
- 并发容器与无锁编程：ConcurrentHashMap、ConcurrentLinkedQueue、CAS 原理（ABA 问题）与解决方案（版本号、AtomicStampedReference）。
- 常见并发问题：死锁、活锁、饥饿、竞态条件，如何定位与修复（线程 dump 分析、锁定位）。

---

## 常见面试题要点（示例）

1. HashMap 为什么要扩容？扩容时发生了什么？
   - 要点：负载因子、threshold；扩容过程会重新计算 index（rehash），链表可能转为红黑树。
   - 面试中可以提性能影响、并发修改导致的问题（JDK7 会出现死循环，JDK8 改进）。

2. synchronized 与 ReentrantLock 区别？
   - 要点：语法形式（内置锁 vs 显式锁）、可重入性、公平性选择、中断响应、条件变量（Condition）。

3. volatile 的作用是什么？能替代 synchronized 吗？
   - 要点：保证可见性和禁止指令重排序（对单个变量的读写原子性，但不能保证复合操作的原子性）。不能替代 synchronized 做复杂同步。

4. 如何定位内存泄漏？
   - 要点：通过 jmap -histo / heap dump（MAT）分析对象保留路径，检查静态集合、线程本地变量、未关闭的资源、长生命周期缓存。

5. 线程池如何选择核心/最大/队列/拒绝策略？
   - 要点：根据任务性质（CPU 密集/IO 密集）、系统容量、响应时间要求调整；优先考虑 bounded 队列与合适的拒绝策略。

---

## 实战案例与练习题（含解题要点）

### 案例 1：实现一个线程安全的 LRU 缓存（容量可控）
- 要求：支持并发读写、get/put 操作，最近最少使用（LRU）淘汰策略。
- 关键点：可用 LinkedHashMap + 重写 removeEldestEntry 实现；要保证并发安全可用 Collections.synchronizedMap 或结合 ConcurrentHashMap + 双向链表 +锁；或使用 LinkedHashMap 放在 synchronized 块里；或者使用 Java 的 ConcurrentLinkedDeque + ConcurrentHashMap 实现无全局锁的高并发 LRU。
- 简要实现思路：
  - 简单实现：`new LinkedHashMap<K,V>(capacity, 0.75f, true)` 并重写 removeEldestEntry，外层使用 `synchronized` 或包装为 `Collections.synchronizedMap`。
  - 高级实现：使用 `ConcurrentHashMap<K,Node>` + `DoublyLinkedList`（手动维护节点顺序），通过分段锁或使用 `ReentrantLock` 保护链表操作以减少竞争。
- 面试答题要点：说明时间复杂度（O(1) get/put）、并发控制策略、内存一致性与可能的性能权衡。

### 案例 2：分析一次 Full GC 并定位内存泄漏
- 场景：线上服务频繁发生 Full GC，响应时延增长，内存占用不断上升直到 OOM。
- 要求：给出排查流程与解决思路。
- 排查步骤：
  1. 收集 GC 日志（-Xlog:gc* 或 -Xlog:gc:gc.log），观察 Young/Full GC 频率与各代占用。
  2. 导出堆快照（jmap -dump:live,file=heap.hprof <pid>）并用 MAT 或 VisualVM 分析 Biggest consumer（Dominators）和 GC Roots。
  3. 查看线程 dump（jstack）排查是否有大量线程/未结束任务导致对象被持有。
  4. 检查代码常见泄漏点：静态集合、ThreadLocal 未清理、缓存无界增长、连接池/资源未关闭、监听器未注销。
- 修复思路：修复泄漏点、添加缓存大小限制、使用弱引用/软引用（场景受限）、改善 GC 策略（如迁移到 G1 并调节堆与代的比例）并监控指标。

### 案例 3：并发场景下的高性能计数器设计
- 题目：实现一个高并发计数器，支持大量线程频繁 increment 和周期性读出总和。
- 要求：低争用、高吞吐。
- 关键点与实现：
  - 简单实现：AtomicLong（存在 CAS 热点，写操作高并发下可能退化）。
  - 更高性能：使用 LongAdder/LongAccumulator（分段计数，减少 CAS 竞争），汇总时再合并各段的值。
  - 面试要点：讲清楚 LongAdder 原理（cells 分散写热点，汇总时成本更高），以及在什么场景下选择哪种方案。

### 案例 4：实现一个可重入的读写锁（简化版）
- 要求：读锁支持多个读者并发，写锁独占；支持可重入（同一线程可重复获取读或写）。
- 关键点：可使用 ReentrantReadWriteLock；若面试要求自实现，可用 `ThreadLocal` 保存重入计数 + `ReentrantLock`/synchronized 结合计数器实现读写逻辑。
- 解题要点：说明如何避免写饥饿、如何实现升降级（写锁升级通常不可行，降级可以通过先获取写锁再获取读锁然后释放写锁实现）。

### 案例 5：集合遍历时并发修改导致异常的解决
- 场景描述：在多线程环境下，用 Iterator 遍历集合时抛出 ConcurrentModificationException；如何修复？
- 解决方案：
  - 使用并发安全集合（CopyOnWriteArrayList、ConcurrentHashMap）根据读多写少或写多读少场景选择。
  - 在单线程上下文用 Collections.synchronizedList 并在外部同步（synchronized(list) {...}）。
  - 在允许弱一致性的场景下，可以遍历集合的 snapshot（集合拷贝）或使用 snapshot 语义的 API。
- 面试要点：指出 fail-fast 的原理（modCount）及其目的是检测并发修改而非作为并发控制手段。

---

## 面试答题建议
- 回答要点化、结构化：先给结论（1-2 句），再给核心原理，最后说明工程实践或权衡。
- 结合场景：面试官更在意你在工程中的取舍（为何选择某个集合或并发方案），要说明性能、可维护性和复杂度。
- 多用图示或伪代码帮助说明复杂流程（例如 HashMap 结构、GC 流程、线程状态转换）。

---

## 参考资料与工具
- 《Java 并发编程实战》
- 《深入理解 Java 虚拟机》
- 官方 JDK 文档与 JEP 说明（GC、内存模型相关）
- 常用工具：jstack、jmap、jstat、jcmd、VisualVM、MAT、async-profiler

---

## 面试题及答案

1. 问：HashMap 为什么要扩容？扩容时发生了什么？
   答：为保证平均 O(1) 的查找效率，HashMap 使用负载因子（默认 0.75）来触发扩容。当 size > threshold 时触发扩容，JDK8 及以后会创建更大的 table 并把已有节点重新分配到新的桶中（重新计算 index）。链表长度超过阈值时会转换为红黑树以降低最坏情况复杂度。从面试角度要说明扩容的开销（需要 rehash、复制数组）以及并发环境下的风险（并发扩容可能导致数据丢失或性能问题）。

2. 问：volatile 的作用是什么？能替代 synchronized 吗？
   答：volatile 保证可见性（写入后其他线程能及时看到）和禁止指令重排序（对该变量的读取/写入不会被重排序到其他内存操作之前或之后）。它不能保证多个操作的原子性（如 i++ 不是原子操作），因此不能完全替代 synchronized。在需要对复合操作或涉及多个变量的同步时，应使用锁（synchronized / ReentrantLock）。

3. 问：ConcurrentHashMap 与 HashMap 的主要区别？并发场景下该如何选择？
   答：HashMap 线程不安全，ConcurrentHashMap 在并发场景下保证线程安全且高性能（JDK8 用 CAS + synchronized + 分段思想实现无全局锁的并发访问）。在高并发读写下应优先使用 ConcurrentHashMap；如果只读多写少且需要强一致性快照，可考虑 CopyOnWriteArrayList/Set 或对整个集合加锁。

4. 问：AtomicLong 和 LongAdder 有什么区别？什么时候用哪种？
   答：AtomicLong 使用单一的 CAS 更新同一个变量，写热点高时 CAS 重试会造成性能下降。LongAdder 采用分段（cells）设计，将更新分散到多个槽以减少竞争，读取总和时需要汇总各槽的值。若写操作极高且对即时精准度要求不高（允许稍微延迟的读取），LongAdder 更适合；对要求严格一致性和读频较高的场景，AtomicLong 更简单且读成本低。

5. 问：synchronized 与 ReentrantLock 的区别？
   答：synchronized 是内置锁，语法简洁，JVM 能做优化（如偏向锁、轻量级锁）；ReentrantLock 是显式锁，支持公平/非公平选项、可中断的锁获取、Condition（多路等待队列）以及更灵活的尝试获取（tryLock）。若需要公平性控制、可中断或多个条件变量，选择 ReentrantLock；普通场景首选 synchronized（更安全、代码更简洁）。

6. 问：如何排查内存泄漏？主要步骤是什么？
   答：步骤：收集堆快照（jmap），分析 heap dump（MAT / VisualVM），查看占用最大的对象与其 GC Roots（who is keeping them alive）。同时检查线程 dump（jstack）看是否有大量线程或任务未结束；审查代码中的常见泄漏点：静态集合、未清理的 ThreadLocal、外部资源未关闭、缓存/监听器/连接池没有边界。解决方法包括修复持有引用、引入缓存大小限制或使用弱引用、改进资源释放流程并增加监控。

7. 问：什么是死锁，如何定位和解决？
   答：死锁是两个或多个线程互相等待对方持有的锁，导致都无法继续执行。定位方法：获取线程 dump（jstack）查看线程状态和锁持有/等待关系（jstack 的输出会指出 deadlock），也可以用 VisualVM 或 async-profiler。解决方法：保证锁获取顺序一致、减少持锁时间、使用 tryLock + 超时避免永久等待，或使用更高层的并发结构（避免手工持有多个锁）。

8. 问：描述 Java 的类加载机制和双亲委派模型。
   答：类加载分为加载、验证、准备、解析、初始化阶段。双亲委派模型中，一个类加载请求首先委派给父加载器，如果父加载器无法加载则由子加载器尝试加载。此机制避免了重复加载核心 Java 类并提高安全性。在特定场景（如热部署、插件系统）可能会自定义类加载器，需注意避免 ClassLoader 泄漏与重复类定义。

9. 问：String 常量池中 == 与 equals 的区别？
   答：`==` 比较对象引用是否相同（是否指向同一地址），`equals` 比较对象的逻辑相等性。String 的字面量会被放入常量池，两个字面量相同的 String 通常引用同一对象（因此 == 为 true），但通过 `new String("x")` 会创建新的对象，== 为 false，需用 equals 比较内容。

10. 问：如何设计一个线程池（ThreadPoolExecutor）参数？
    答：根据任务特性选择：
    - CPU 密集型：核心线程数 ≈ CPU 核数（n），避免创建过多线程。
    - IO 密集型：核心线程数可 > CPU 核数，视 IO 等待比例增加线程数。
    - 队列选择：SynchronousQueue（直交给线程）适合短任务并快速扩容，ArrayBlockingQueue/LinkedBlockingQueue 适合缓冲；使用有界队列避免 OOM。
    - 拒绝策略：在达到最大容量时选择合适策略（AbortPolicy/CallerRunsPolicy/DiscardPolicy/DiscardOldestPolicy）。

11. 问：什么是 Java 内存模型（JMM）中的 happens-before 规则？
    答：happens-before 是一组保证操作可见性与有序性的规则，若操作 A happens-before 操作 B，则 A 的结果对 B 可见。常见的 happens-before 包括：程序顺序规则、监视器锁入/解锁、volatile 读/写、线程 start/join、传递性等。理解该规则对正确并发设计非常重要。

12. 问：如何分析一次 Full GC 并减少 Full GC 频率？
    答：分析步骤：查看 GC 日志（-Xlog:gc*），定位 GC 类型、停顿时间、各代占用及晋升失败原因；结合堆快照判断大对象或长寿命对象。减少策略：调大堆或年轻代大小，调整晋升阈值（-XX:MaxTenuringThreshold），使用更适合的收集器（G1）、修复应用层内存泄漏或控制缓存大小。


---

