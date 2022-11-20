import pytest
import os
import configparser as parser
from controller.remote_controller import RemoteController
from time import sleep


@pytest.fixture
def configure() -> parser.ConfigParser:
    """
    :pytest - Pytest fixture to configure and 
              return configparser in order to read
              config.ini file
    """
    return parser.ConfigParser()
    
    
@pytest.fixture
def host(configure: parser.ConfigParser) -> str:
    """
    :pytest - Pytest Fixture that reads for the 
              IP value from the config.ini file.
    """
    configure.read('config.ini')
    return configure.get('conn','ip')

@pytest.fixture
def port(configure: parser.ConfigParser) -> str:
    """
    :pytest - Pytest Fixture that reads from the 
              config.ini file to retrieve the port
              on which Roku is listening to.
    """
    configure.read('config.ini')
    return configure.get('conn','port')

@pytest.fixture
def controller(host: str, port: str) -> RemoteController:
    """
    :pytest - Pytest Fixture used to instantiate the 
              remotes controller in order to send commands
              via HTTP protocol to Roku.
    """
    return RemoteController(host, port)


def test_down_key(controller: RemoteController) ->None:
    """
    :pytest - Pytest used to test the controllers
              down key functionality. If OK status
              code 200 returned
    :param - RemoteController
    """
    response = controller.down()
    assert response.status_code == 200
    sleep(5)

def test_up_key(controller: RemoteController) -> None:
    """
    :pytest - Pytest used to test the controllers
              up key functionality. If OK status
              code 200 returned
    :param - RemoteController
    """
    response = controller.up()
    assert response.status_code == 200
    sleep(5)

def test_left_key(controller: RemoteController) -> None:
    """
    :pytest - Pytest used to test the controllers
              left key functionality. If OK status
              code 200 returned
    :param - RemoteController
    """
    response = controller.left()
    assert response.status_code == 200
    sleep(5)

def test_right_key(controller: RemoteController) -> None:
    """
    :pytest - Pytest used to test the controllers
              right key functionality. If OK status
              code 200 returned
    :param - RemoteController
    """
    response = controller.right()
    assert response.status_code == 200
    sleep(5)

def test_back_key(controller: RemoteController) -> None:
    """
    :pytest - Pytest used to test the controllers
              back key functionality. If OK status
              code 200 returned
    :param - RemoteController
    """
    response = controller.back()
    assert response.status_code == 200
    sleep(5)

