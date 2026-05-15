# обход блокировок
# Загрузка с индикацией выполнения и обработкой ошибок
import time

from tqdm import tqdm


def main():
    for _ in tqdm(range(1000)):
        time.sleep(0.01)


if __name__ == '__main__':
    main()
