Metranome
=========

Metranome is a timer for AMQP systems. It exists to replace using Cron to
signal starting a task.

Cron works well for single servers although becomes more difficult to manage
when multiple computers and processes are used. Metranome allows you to have a
single signal to begin a task.

Using Metranome
===============

Metranome will publish an event every minute. Listeners can bind to the topic
exchange `metranome` with the routing key matching the
`year.month.day.hour.minute`.

If you want a task to run every minute bind to: `*.*.*.*.*`.

If you want a task to run every hour bind to: `*.*.*.*.0`.

If you want a task to run every 5 minutes bind to:

```
*.*.*.*.0
*.*.*.*.5
*.*.*.*.10

...

*.*.*.*.55
```
