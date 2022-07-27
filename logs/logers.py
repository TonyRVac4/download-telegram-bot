from loguru import logger


def downloader_loger(exception: Exception, text: str) -> None:
    logger.add("logs/logs.log", retention="2 days", level='DEBUG')
    logger.debug(f"Exception: |--{exception}--|\nurl = '{text}'\n")
