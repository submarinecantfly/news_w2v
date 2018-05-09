from lib.write_result import write_result
from lib.calc_test_data import calc_test_data
from lib.train_model import train_model

def main():
    train_model()
    calc_test_data()
    write_result()
    print('top20 done')

if __name__ == "__main__":
    main()