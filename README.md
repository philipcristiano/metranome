Metranome
=========

Metranome is a timer for AMQP systems, like a metronome. It exists to replace
using Cron to signal starting a task.

Cron works well for single servers although becomes more difficult to manage
when multiple computers and processes are used. Metranome allows you to have a
single signal to begin a task.

Using Metranome
===============

Metranome will publish an event every minute. Listeners can bind to the topic
exchange `metranome` with the routing key matching the
`year.month.day_of_week_int.day.hour.minute`.

`day_of_week_int` is 0-6, Monday-Sunday.

If you want a task to run every minute bind to: `*.*.*.*.*.*`.

If you want a task to run every hour bind to: `*.*.*.*.*.0`.

If you want a task to run every 5 minutes bind to:

```
*.*.*.*.*.0
*.*.*.*.*.5
*.*.*.*.*.10

...

*.*.*.*.*.55
```

Hacking Metranome
=================

* Clone the project
* Copy `local.config.example` to `local.config` and add your RabbitMQ host
* Make the development environment `make virtualenv requirements`
* Hack away!

Useful:
You can run tests `make test`
Run Metranome `make main`
