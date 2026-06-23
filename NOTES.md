Pip and uv are both tools designed to intertact with Pypi to install packages that is needed for a project

--PIP--
helps us to create a virtual environment for a project and it needs to be activated seperately 

it executes tasks sequentially

needs seperate tools like "pip-tools" for dependency locking


--UV--
helps to create a virtual environment 
uv is 10-100 times faster than pip 
uses RUST implementation that helps to execute tasks parallely
                                    efficient handling of large dependency tree
                                    has build in locks
                                    had pyproject.toml to store built settings and tool configurations, 
                                       projects meta data.