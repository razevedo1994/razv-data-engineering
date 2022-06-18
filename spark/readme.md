# Spark Application Concepts

- `Application`: A user program built on Spark using APIs. It consists of a driver program and executors on the cluster.

- `SparkSession`: An object that provides a point of entry to interact with underlying Spark functionality and allows programming Spark with its APIs. In an interactive Spark shell, the Spark driver instantiates a SparkSession for you, while in a Spark applications, you create a SparkSession object yourself.

- `job`: A parallel computation consisting of multiple tasks that gets spawned in response to a Spark action (e.g., save(), collect()).

- `Stage`: Each job gets divided into smaller sets of tasks called stages that depend on each other.

- `Task`: A single unit of work or execution that will be sent to a Spark executor.

## Spark Application and SparkSession

At the core of every Spark Application is the Spark driver program, which creates a SparkSession object. When you're working with a Spark shell, the driver is part of the shell and the SparkSession object (accessible via the variable spark) is created for you. Once you have a SparkSession, you can program Spark using the APIs.

[Starting Point: SparkSession](https://bityl.co/ClfV)

## Spark Jobs

During interactive session with Spark shells, the driver converts your Spark application into one or more Spark jobs. It then transform each job into a DAG. This, in essence, is Spark's execution plan, where each node within a DAG could be a single or multiple Spark stages.

## Spark Stages

As part of the DAG nodes, stages are created based on what operations can be performed serially or in parallel. Not all Spark operations can happen in a single stage, so they may be divided into multiple stages. Often stages are delineated on the operator's computation boundaries, where they dictate data transfer among Spark executors.

## Spark Tasks

Each stage is comprised os Spark tasks (a unit os execution), which are then federated across each Spark executor; each task maps to a single core and works on a single partition of data. As such, an executor with 16 cores can have 16 or more tasks working on 16 or more partitions in parallel, making the execution os Spark's tasks exceedingly parallel.
#
# Transformations, Action, and Lazy Evaluation

Spark operations on distributed data can be classified into two types: `transformations` and `actions`. Transformations, as the name suggests, transform a Spark Dataframe into a new DataFrame without altering the original data, giving it the property of immutability. Put another way, an operation such as `select()` or `filter()` will not change the original DataFrame; instead, it will return the transformed results of the operation as a new DataFrame.

All transformation are evaluated lazily. That is, their results are not computed immediately, but they are recorded or remembered as a linegae. A recorded lineage allows Spark, at a later time in its execution plan, to rearrange certain transformations, coalesce them, or optimeze transformations into stages for more efficient execution. Lazy evaluation is Spark's strategy for delaying execution until an action is invoked or data is "touched" (read from or written to disk).

While lazy evaluation allows Spark to optimize your queries by peeking into your chained transformations, lineage and data immutability provide fault tolerance.

- Transformations: `orderBy()`, `groupBy()`, `filter()`, `select()`, `join()`

- Actions: `show()`, `take()`, `count()`, `collect()`, `save()`
#

# Narrow and Wide Transformations




