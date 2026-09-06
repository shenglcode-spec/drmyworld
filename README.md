<div align="center">

# Hello, I'm drmyworld 👋

### 8 年 Java 开发工程师 · 热爱代码 · 追求极致

</div>

---

## 关于我

- 🎯 拥有 **8 年** Java 后端开发经验，深耕企业级应用与分布式系统
- 🏗️ 擅长高并发架构设计、性能优化与系统稳定性建设
- 🌱 持续学习云原生、微服务架构与前沿技术
- ✍️ 乐于分享技术心得，相信交流让成长更快

---

## 技术栈

### 编程语言

![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)

### 框架 & 组件

![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=spring-boot&logoColor=white)
![Spring Cloud](https://img.shields.io/badge/Spring_Cloud-6DB33F?style=flat-square&logo=spring&logoColor=white)
![MyBatis](https://img.shields.io/badge/MyBatis-000000?style=flat-square&logo=mybatis&logoColor=white)
![Spring Security](https://img.shields.io/badge/Spring_Security-6DB33F?style=flat-square&logo=spring&logoColor=white)

### 数据库 & 中间件

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apache-kafka&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white)

### 高斯数据库 & 国产化

![GaussDB](https://img.shields.io/badge/GaussDB-CF0A2C?style=flat-square&logo=databricks&logoColor=white)
![GaussDB_for_MySQL](https://img.shields.io/badge/GaussDB(for_MySQL)-CF0A2C?style=flat-square&logo=mysql&logoColor=white)
![GaussDB_for_PG](https://img.shields.io/badge/GaussDB(for_PostgreSQL)-CF0A2C?style=flat-square&logo=postgresql&logoColor=white)
![openGauss](https://img.shields.io/badge/openGauss-CF0A2C?style=flat-square&logo=opensourceinitiative&logoColor=white)
![Data_Studio](https://img.shields.io/badge/Data_Studio-CF0A2C?style=flat-square&logo=databricks&logoColor=white)

### DevOps & 工具

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

---

## GitHub 统计

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=drmyworld&show_icons=true&count_private=true&hide_border=true&theme=graywhite&bg_color=ffffff" alt="GitHub Stats" height="180" />

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=drmyworld&layout=compact&hide_border=true&theme=graywhite&bg_color=ffffff" alt="Top Languages" height="180" />

<img src="https://github-readme-streak-stats.herokuapp.com/?user=drmyworld&hide_border=true&theme=graywhite&background=ffffff" alt="GitHub Streak" height="180" />

</div>

---

## 面试常见问题

> 点击题目展开答案，持续更新中…

### ☕ Java 基础 & JVM

<details>
<summary><b>Q1：HashMap 的底层实现原理？JDK 1.7 和 1.8 有什么区别？</b></summary>

- **1.7**：数组 + 链表，头插法，扩容时会导致链表反转，并发下可能形成环形链表造成死循环。
- **1.8**：数组 + 链表 + 红黑树，尾插法，当链表长度 ≥ 8 且数组长度 ≥ 64 时转为红黑树（查询复杂度从 O(n) 降为 O(logn)），解决了并发死循环问题（但仍非线程安全）。
- **扩容**：默认容量 16，负载因子 0.75，每次扩容为原来的 2 倍，元素重新计算 hash 落点（1.8 优化为原位或原位 + oldCap）。
</details>

<details>
<summary><b>Q2：JVM 内存区域如何划分？哪些是线程私有的？</b></summary>

- **线程私有**：程序计数器、虚拟机栈、本地方法栈。
- **线程共享**：堆、方法区（JDK 8 后改为元空间 Metaspace，使用本地内存）。
- **直接内存**：NIO 相关，不受堆大小限制，但受物理内存限制。
- 常见 OOM：堆 OOM、栈溢出 StackOverflowError、元空间 OOM、直接内存 OOM。
</details>

<details>
<summary><b>Q3：说一下 JVM 的垃圾回收算法和常用垃圾收集器？</b></summary>

- **算法**：标记-清除、标记-复制、标记-整理、分代收集。
- **收集器**：
  - Serial / ParNew：新生代，复制算法。
  - CMS：老年代，标记-清除，低延迟，有内存碎片问题。
  - G1：Region 化内存，可预测停顿时间，JDK 9 默认。
  - ZGC：超低延迟（< 10ms），JDK 11+。
</details>

<details>
<summary><b>Q4：双亲委派模型是什么？为什么要这样设计？</b></summary>

- 类加载时先委托父加载器加载，父加载器无法加载时才自己加载。
- **作用**：避免类的重复加载，保护核心 API 不被篡改（如用户自定义 `java.lang.String` 不会被加载）。
- **打破场景**：SPI（如 JDBC）、Tomcat 多应用隔离、OSGi、热部署等。
</details>

### 🔒 Java 并发编程

<details>
<summary><b>Q5：synchronized 和 ReentrantLock 的区别？</b></summary>

| 特性 | synchronized | ReentrantLock |
|------|-------------|---------------|
| 实现 | JVM 层面 | JDK 层面（AQS） |
| 释放 | 自动释放 | 需手动 unlock |
| 公平性 | 非公平 | 可公平/非公平 |
| 中断 | 不可中断 | 可中断（lockInterruptibly） |
| 条件变量 | 单一 wait/notify | 支持多个 Condition |
| 尝试获取锁 | 不支持 | tryLock |
</details>

<details>
<summary><b>Q6：volatile 的作用？能保证原子性吗？</b></summary>

- **作用**：保证可见性（强制读写主内存）、禁止指令重排序（内存屏障）。
- **不能保证原子性**：如 `i++` 实际是读-改-写三步，volatile 不能防止多线程下的丢失更新。
- 典型场景：双重检查锁单例中的 `instance` 变量、状态标志位。
</details>

<details>
<summary><b>Q7：ThreadLocal 的原理和内存泄漏问题？</b></summary>

- 每个 Thread 有一个 `ThreadLocalMap`，key 为 ThreadLocal 的弱引用，value 为强引用。
- **内存泄漏**：ThreadLocal 被回收后，key 变为 null，但 value 仍被强引用无法回收。
- **解决**：使用完后手动调用 `remove()`，或使用线程池时务必清理。
</details>

<details>
<summary><b>Q8：线程池的核心参数？拒绝策略有哪些？</b></summary>

- **核心参数**：corePoolSize、maximumPoolSize、keepAliveTime、workQueue、threadFactory、handler。
- **执行流程**：核心线程 → 队列 → 最大线程 → 拒绝策略。
- **拒绝策略**：
  - AbortPolicy（默认，抛异常）
  - CallerRunsPolicy（调用者线程执行）
  - DiscardPolicy（直接丢弃）
  - DiscardOldestPolicy（丢弃队列最老任务）
</details>

### 🍃 Spring & Spring Boot

<details>
<summary><b>Q9：Spring Bean 的生命周期？</b></summary>

1. 实例化（Instantiation）
2. 属性赋值（Populate）
3. 调用 Aware 接口方法（BeanNameAware、BeanFactoryAware 等）
4. BeanPostProcessor 前置处理（postProcessBeforeInitialization）
5. 初始化（@PostConstruct → InitializingBean → init-method）
6. BeanPostProcessor 后置处理（AOP 代理在此生成）
7. 使用
8. 销毁（@PreDestroy → DisposableBean → destroy-method）
</details>

<details>
<summary><b>Q10：Spring 的循环依赖如何解决？</b></summary>

- **三级缓存**：
  - 一级缓存 singletonObjects：成品 Bean
  - 二级缓存 earlySingletonObjects：半成品（已实例化未初始化）
  - 三级缓存 singletonFactories：ObjectFactory 工厂（用于 AOP 代理）
- **流程**：A 实例化后放入三级缓存 → A 注入 B → B 实例化 → B 注入 A 时从三级缓存拿到 A 的早期引用 → B 完成 → A 完成。
- **限制**：只能解决单例 setter 注入的循环依赖，构造器注入和 prototype 作用域无法解决。
</details>

<details>
<summary><b>Q11：Spring Boot 自动装配原理？</b></summary>

- 核心注解 `@SpringBootApplication` 包含 `@EnableAutoConfiguration`。
- 通过 `@Import(AutoConfigurationImportSelector.class)` 加载 `spring.factories`（Spring Boot 2.7+ 改为 `AutoConfiguration.imports`）中配置的自动配置类。
- 结合 `@ConditionalOnXxx` 条件注解，按需装配 Bean。
</details>

<details>
<summary><b>Q12：Spring 事务失效的常见场景？</b></summary>

1. 方法非 public（Spring AOP 基于 public 方法）
2. 同类内部方法调用（未经过代理对象）
3. 异常类型不匹配（默认只回滚 RuntimeException 和 Error）
4. try-catch 吞掉了异常
5. 数据库引擎不支持事务（如 MyISAM）
6.  propagation 设置错误（如 NEVER、NOT_SUPPORTED）
</details>

### 🗄️ 数据库 & 中间件

<details>
<summary><b>Q13：MySQL 索引底层数据结构？为什么用 B+ 树而不是 B 树？</b></summary>

- **B+ 树**：非叶子节点只存索引不存数据，叶子节点存储数据并通过双向链表连接。
- **相比 B 树**：
  - 非叶子节点不存数据，单节点可存更多索引 → 树更矮 → IO 更少
  - 叶子节点链表，范围查询效率高
  - 查询稳定（每次都走到叶子节点）
</details>

<details>
<summary><b>Q14：MySQL 事务隔离级别？MVCC 如何实现？</b></summary>

- **隔离级别**：读未提交 → 读已提交（RC）→ 可重复读（RR，MySQL 默认）→ 串行化。
- **MVCC**：通过隐藏字段（trx_id、roll_pointer）、undo log 版本链、ReadView 实现。
- RC 每次 SELECT 生成新 ReadView，RR 仅第一次 SELECT 生成（解决不可重复读）。
- RR 下配合 Next-Key Lock（Gap Lock + Record Lock）解决幻读。
</details>

<details>
<summary><b>Q15：Redis 为什么快？有哪些数据结构？</b></summary>

- **快的原因**：纯内存操作、单线程避免上下文切换、IO 多路复用、高效数据结构。
- **核心数据结构**：String、Hash、List、Set、ZSet。
- **底层编码**：SDS、ZipList、QuickList、Dict、SkipList、IntSet 等。
</details>

<details>
<summary><b>Q16：Redis 缓存穿透、击穿、雪崩的区别与解决方案？</b></summary>

- **穿透**：查询不存在的数据。→ 缓存空值、布隆过滤器。
- **击穿**：热点 key 过期瞬间大量请求打 DB。→ 互斥锁、热点 key 永不过期。
- **雪崩**：大量 key 同时过期或 Redis 宕机。→ 过期时间加随机值、多级缓存、Redis 集群高可用。
</details>

<details>
<summary><b>Q17：GaussDB 相比 MySQL 有哪些优势和差异？</b></summary>

- **优势**：
  - 支持行列混合存储（OLTP + OLAP 一体化），分析查询性能更强
  - 内置 AI 能力（AI4DB、DB4AI），如智能索引推荐、性能自调优
  - 国产化适配，支持鲲鹏芯片，满足信创要求
  - 支持分布式部署（Shared-Nothing），水平扩展能力强
- **差异**：
  - GaussDB 语法兼容 PostgreSQL，部分与 MySQL 有差异
  - 事务隔离级别默认为读已提交（RC），与 MySQL 默认 RR 不同
  - 锁机制更细粒度，支持 MVCC + 行级锁
</details>

### 🌐 分布式 & 微服务

<details>
<summary><b>Q18：分布式事务有哪些解决方案？</b></summary>

- **2PC / 3PC**：强一致性，性能差，存在阻塞和单点问题。
- **TCC**：Try-Confirm-Cancel，业务侵入性强，性能较好。
- **Saga**：长事务补偿，适合跨服务业务流程。
- **本地消息表 + MQ**：最终一致性，业务侵入小。
- **Seata**：AT 模式（自动补偿）、TCC、Saga、XA 四种模式。
</details>

<details>
<summary><b>Q19：分布式锁的实现方式及优缺点？</b></summary>

- **Redis**：`SETNX + EX`，简单高效，但需注意锁续期（Redisson 看门狗）和 RedLock 问题。
- **ZooKeeper**：临时顺序节点，天然支持锁等待和释放通知，但性能一般。
- **MySQL**：乐观锁（版本号）、悲观锁（for update），简单但性能差。
- 生产推荐 Redisson（自动续期 + 可重入）。
</details>

<details>
<summary><b>Q20：Kafka 如何保证消息不丢失、不重复、有序性？</b></summary>

- **不丢失**：生产者 acks=all + 重试；Broker 副本机制；消费者手动提交 offset。
- **不重复（幂等）**：生产者开启幂等（`enable.idempotence=true`）；消费者业务侧幂等（唯一 ID + 去重表）。
- **有序性**：单分区内有序；相同 key 的消息路由到同一分区。
</details>

### 🚀 JVM 调优专题

<details>
<summary><b>Q21：JVM 调优常用参数有哪些？如何排查 OOM？</b></summary>

- **常用参数**：
  - 堆大小：`-Xms`（初始堆）、`-Xmx`（最大堆），建议两者设为相同避免动态扩容
  - 新生代：`-Xmn` 或 `-XX:NewRatio`、`-XX:SurvivorRatio`
  - 元空间：`-XX:MetaspaceSize`、`-XX:MaxMetaspaceSize`
  - GC 日志：`-Xlog:gc*`（JDK 9+）或 `-XX:+PrintGCDetails`
  - OOM dump：`-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/heap.hprof`
- **排查 OOM 步骤**：
  1. 通过 `jstat -gc` 观察 GC 频率和各区域使用率
  2. 用 `jmap -dump` 或 OOM 自动 dump 生成堆快照
  3. 用 MAT / VisualVM 分析 dump，定位大对象和内存泄漏点
  4. 检查是否有静态集合持有对象、ThreadLocal 未 remove、流未关闭等
</details>

<details>
<summary><b>Q22：强引用、软引用、弱引用、虚引用的区别及使用场景？</b></summary>

| 引用类型 | GC 回收时机 | 使用场景 |
|---------|------------|---------|
| 强引用 | 不回收（只要引用存在） | 普通对象引用 |
| 软引用 SoftReference | 内存不足时回收 | 内存敏感的缓存 |
| 弱引用 WeakReference | 下次 GC 一定回收 | WeakHashMap、ThreadLocal key |
| 虚引用 PhantomReference | 随时可能回收 | 管理堆外内存，必须配合 ReferenceQueue |
</details>

### ⚡ MySQL 性能优化

<details>
<summary><b>Q23：如何排查和优化 MySQL 慢查询？</b></summary>

1. **开启慢查询日志**：`slow_query_log=ON`，`long_query_time=1`
2. **定位慢 SQL**：`mysqldumpslow` 或 `pt-query-digest` 分析日志
3. **EXPLAIN 分析执行计划**：关注 `type`（ALL→index→range→ref→eq_ref→const）、`key`、`rows`、`Extra`
4. **优化手段**：
   - 添加合适索引（覆盖索引、联合索引最左前缀）
   - 避免 `SELECT *`、避免索引列上使用函数/运算
   - 大表分页优化：`WHERE id > last_id LIMIT N` 替代 `LIMIT offset, N`
   - 优化 JOIN：小表驱动大表，确保 JOIN 字段有索引
   - 分库分表、读写分离
5. **配置优化**：`innodb_buffer_pool_size`（物理内存 50%~70%）、`innodb_log_file_size`、连接池等
</details>

<details>
<summary><b>Q24：什么是索引下推（ICP）？什么是覆盖索引？</b></summary>

- **索引下推（Index Condition Pushdown）**：MySQL 5.6+ 优化，在存储引擎层利用索引过滤数据，减少回表次数。例如联合索引 `(a, b)`，查询 `WHERE a=1 AND b=2`，可在索引层面直接过滤 b 的条件。
- **覆盖索引**：查询的列全部包含在索引中，无需回表查询聚簇索引。`EXPLAIN` 的 `Extra` 显示 `Using index`。
- **示例**：表有索引 `(name, age)`，查询 `SELECT name, age FROM user WHERE name='张三'` 即为覆盖索引，效率极高。
</details>

### 🌥️ Spring Cloud 微服务

<details>
<summary><b>Q25：Spring Cloud 核心组件有哪些？各自作用？</b></summary>

| 组件 | 作用 |
|------|------|
| Eureka / Nacos | 服务注册与发现 |
| Ribbon / LoadBalancer | 客户端负载均衡 |
| Feign / OpenFeign | 声明式 HTTP 调用 |
| Hystrix / Sentinel | 熔断、降级、限流 |
| Gateway / Zuul | API 网关 |
| Config / Nacos Config | 分布式配置中心 |
| Sleuth + Zipkin | 链路追踪 |
| Bus | 消息总线（配置刷新） |
</details>

<details>
<summary><b>Q26：服务熔断、降级、限流的区别？Sentinel 如何实现？</b></summary>

- **熔断**：下游服务故障时，快速失败，避免级联故障（如 Hystrix/Sentinel 熔断）。
- **降级**：系统压力大时，关闭非核心功能，保证核心功能可用。
- **限流**：控制单位时间内的请求数量，保护系统不被冲垮。
- **Sentinel 实现**：
  - 基于滑动窗口统计 QPS、线程数等指标
  - 支持流量控制（直接、关联、链路）、熔断降级（慢调用比例、异常比例、异常数）、热点参数限流
  - 控制台可动态配置规则
</details>

<details>
<summary><b>Q27：Nacos 和 Eureka 的区别？Nacos 的 CP 和 AP 模式？</b></summary>

| 特性 | Eureka | Nacos |
|------|--------|-------|
| CAP | AP | 支持 AP + CP 切换 |
| 健康检查 | 客户端心跳 | 心跳 + 主动探测 |
| 配置中心 | 无（需 Spring Cloud Config） | 内置 |
| 控制台 | 弱 | 强（支持权重、命名空间） |
| 维护状态 | 停更（2.0 停止开发） | 活跃（阿里开源） |
- **AP 模式**：可用性优先，临时实例（DEFAULT 模式），服务异常直接摘除。
- **CP 模式**：一致性优先，持久化实例，使用 Raft 协议，需主动注销服务。
</details>

### 🎨 设计模式

<details>
<summary><b>Q28：单例模式的实现方式？为什么推荐枚举单例？</b></summary>

- **实现方式**：
  1. 饿汉式：类加载即创建，线程安全，但浪费内存
  2. 懒汉式：按需创建，需加锁（DCL 双重检查锁 + volatile）
  3. 静态内部类：利用类加载机制保证线程安全，延迟加载
  4. 枚举：JVM 保证单例，防止反射和序列化破坏
- **推荐枚举的原因**：
  - 代码简洁，线程安全由 JVM 保证
  - 天然防止反射攻击（`newInstance` 抛异常）
  - 天然防止序列化破坏（反序列化返回同一实例）
</details>

<details>
<summary><b>Q29：Spring 中用到了哪些设计模式？</b></summary>

- **工厂模式**：BeanFactory、FactoryBean
- **单例模式**：Spring Bean 默认单例
- **代理模式**：AOP（JDK 动态代理 / CGLIB）
- **模板方法**：JdbcTemplate、RestTemplate、RedisTemplate
- **观察者模式**：ApplicationEvent / ApplicationListener
- **策略模式**：InstantiationStrategy、ResourceLoader
- **适配器模式**：AdvisorAdapter、HandlerAdapter
- **装饰器模式**：BeanWrapper、HttpServletRequestWrapper
</details>

<details>
<summary><b>Q30：责任链模式的原理？在哪些框架中应用？</b></summary>

- **原理**：将请求沿处理者链传递，每个处理者决定是否处理或转发给下一个，解耦请求发送者和处理者。
- **应用场景**：
  - Spring Security：过滤器链 FilterChain
  - Servlet：Filter 链
  - Netty：ChannelPipeline / ChannelHandler
  - Spring AOP：拦截器链
- **优点**：灵活组合处理逻辑，易于扩展；**缺点**：可能导致处理延迟，链路过长影响性能。
</details>

<details>
<summary><b>Q31：动态代理的实现方式？JDK 代理和 CGLIB 的区别？</b></summary>

| 特性 | JDK 动态代理 | CGLIB |
|------|-------------|-------|
| 原理 | 基于接口，生成实现接口的代理类 | 基于继承，生成目标类的子类 |
| 目标类要求 | 必须实现接口 | 不能是 final 类/方法 |
| 核心类 | `Proxy`、`InvocationHandler` | `Enhancer`、`MethodInterceptor` |
| 性能 | 创建快、调用稍慢 | 创建慢、调用快（FastClass） |
| Spring 默认 | 有接口时使用 | 无接口时使用 |
- Spring Boot 2.x 起默认使用 CGLIB（可通过 `spring.aop.proxy-target-class=false` 切换为 JDK 代理）。
</details>

---

## 精选项目

<div align="center">

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=drmyworld&repo=drmyworld&hide_border=true&theme=graywhite&bg_color=ffffff)](https://github.com/drmyworld/drmyworld)

</div>

> 💡 想在此展示你的开源项目？将上方 `repo=drmyworld` 替换为你的仓库名即可，可复制多份展示多个项目。

---

<div align="center">

*感谢你抽出时间浏览我的主页，期待与你交流！* ✨

</div>
