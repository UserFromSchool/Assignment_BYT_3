# Assignment_BYT_3
Assignment number 3 from BYT classes. Implemented in python. The tasks are in the folders `part-one-py` and `part-two-py`. The `part-one-cs-example` was only used for copying and code comparison. Tests are implemented with `pytest` library. Use this code
snippet to run quickly:</br>
**MacOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt
pytest  # Will automatically locate the tests
```
**Windows**
```shell
python3 -m venv .venv
./venv/Scripts/Activate
pip install -r requirement.txt
pytest  # Will automatically locate the tests
```
The `shapes.py` and `calculator.py` both can be run as main files and will show the functionality.<br/><br/>
Note: Task implied the operation and calculation should be done in the initializaiton. I was not sure if I understand correctly and how would that
work, so ended up doing operation setting at initialization and then calculations done at calling the class using the operation.