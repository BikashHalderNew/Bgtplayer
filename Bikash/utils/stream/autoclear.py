import os

from Bikash.config import autoclean

async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean_copy = autoclean.copy()
        for item in autoclean_copy:
            if item == rem:
                autoclean.remove(item)

        count = autoclean.count(rem)
        if count == 0:
            if (
                "vid_" not in rem
                and "live_" not in rem
                and "index_" not in rem
            ):
                try:
                    if os.path.exists(rem):
                        os.remove(rem)
                except:
                    pass
    except:
        pass
