import pytest
#session()    module()  class()   function()
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    print('接口测试开始')
    yield
    print('结束')