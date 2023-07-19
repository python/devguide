.. _using-codespaces:
.. _codespaces:

===================================
Contribute Using Github Codespaces
===================================

.. _codespaces-whats-codespaces:

What is Github Codespaces
-------------------------
  
If you'd like to start contributing to CPython without needing to set up a local developer environment, you can use `Github Codespaces <https://github.com/features/codespaces>`_.
Codespaces is a cloud-based development environment offered by GitHub that allows developers to write, build, test, and debug code directly within their web browser or in Visual Studio Code (VS Code).  

To help you get started CPython contains a `devcontainer folder <https://github.com/python/cpython/tree/main/.devcontainer>`_ with a json file that provides consistent and versioned codespace configurations for all users of the project. 
It also contains a docker file that allows you to set up the same environment but locally in a docker container if you'd prefer to do that.

.. _codespaces-create-a-codespace:

Create A CPython Codespace
--------------------------       

Here are the basic steps needed to contribute a patch using Codespaces.
You first need to navigate to the `CPython repo <https://github.com/python/cpython>`_ hosted on GitHub.

Then you will need to:

1. Click the green :guilabel:`Code` button and choose the `codespaces` tab.
2. Press the green :guilabel:`create a new codespace on main` button.
3. A screen should appear that lets you know your codespace is being set up. (Note: Since the CPython devcontainer is provided codespaces will use the configurations it specifies.) 
4. VS Code will open inside of your web browser, already linked up with your code and a terminal to the remote codespace.
5. Use the terminal with the usual git commands to create a new branch, commit and push your changes once you're ready!

If you close your repository and come back later you can always resume your codespace by navigating to the CPython repo, selecting the codespaces tab and selecting your most recent codespaces session. 
You should then be able to pick up from where you left off! 

.. _codespaces-use-locally:

Use Codespaces Locally
-----------------------  
 
On the bottom left side of the codespace screen you will see a green or grey square that says :guilabel:`Codespaces`. 
You can click on this for additional options. If you prefer working on a locally installed copy of VS Code you can select the option `Open in VS Code`. 
You will still be working on the remote codespace instance, thus utilising the remote instance compute power.
The compute power may be a much higher spec than your local machine which can be helpful.


.. TODO: add docker instructions 
