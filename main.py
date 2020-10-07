import os
import sys
import json
import logging
from random import sample

from pyperclip import copy


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


logger = logging.getLogger("FuckWorm")


def load_config() -> dict:
    try:
        with open(f"{os.getcwd()}\\config.json", "r", encoding='utf-8') as file:
            try:
                config = json.load(file)
            except json.JSONDecodeError:
                logger.exception("读取配置文件错误")
                exit(1)
            else:
                return config
    except FileNotFoundError:
        logger.exception(f"配置文件不存在：使用默认配置")

        config = {"append_tags_num": 6, "tags": list()}
        return config


def save_config(config: dict):
    with open(f"{os.getcwd()}/config.json", "w", encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False, indent=4)
    logger.info("成功保存配置")


def get_rand_tags(tags: set, num: int):
    return sample(tags, min(num, len(tags)))


if __name__ == "__main__":
    config = load_config()

    try:
        tags = set(config["tags"])
    except:
        tags = set()

    if tags == None or len(tags) == 0 or sys.argv.count("-t"):
        print("请输入 tag，一行一个，输入空行结束")

        while True:
            tag = input()

            if tag == "":
                break

            if tag[0] == "#":
                tags.add(tag)

        config["tags"] = list(tags)
        save_config(config)

    if sys.argv.count("-n"):
        try:
            config["append_tags_num"] = int(sys.argv[sys.argv.index("-n") + 1])
        except:
            pass

        save_config(config)

    if sys.argv.count("-p"):
        logger.info(config)

    text = str()
    while True:
        if text == "":
            print("请输入要发送的文字，输入 exit 退出")
            text = input()

        if text == "exit":
            break

        tags_text = ""
        for tag in get_rand_tags(tags, config["append_tags_num"]):
            tags_text = tags_text + f"\n{tag}"

        cut_length = 140 - len(tags_text)
        cut_text = text[:cut_length - 1]
        text = text[cut_length:]

        print(cut_text + tags_text)
        copy(cut_text + tags_text)
