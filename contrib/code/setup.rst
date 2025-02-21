==================
Setup and building
==================

.. important::

   |draft|

   |purpose|

[More setup and build instructions specifically for code contributors, building
on the basics from the :ref:`Getting Started <getting-started>` section.]

.. _configure-cache:

Using Configure Cache (`configure -C`)
--------------------------------------

### Overview  
When running `./configure`, CPython performs a series of system checks to detect platform-specific settings. These checks can be time-consuming, especially for repeated builds.  

By using **configure cache (`-C`)**, you can store previous configuration results, reducing redundant checks and **significantly speeding up build times**.  

### Benefits of `configure -C`  
- **Faster rebuilds**: Skips redundant system checks, improving efficiency.  
- **Improves development workflow**: Optimizes the edit-configure-build-test cycle.  
- **Reduces system load**: Avoids unnecessary reconfigurations.  

### How to Use `configure -C`  
To enable caching, run:  
```sh
./configure -C