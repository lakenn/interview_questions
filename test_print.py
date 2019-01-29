import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Youyu Score File')
    parser.add_argument('-f', '--file', help='filename', required=True)
    parser.add_argument('-c', '--color', required=True)

    cmd_line_result = parser.parse_args()
    print('Color is' )