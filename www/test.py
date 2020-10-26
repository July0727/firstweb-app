import orm
import asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')

    u = User(name='Allen', email='0001@qq.com',
             passwd='1234', image='about:blank')

    await u.save()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
