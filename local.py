from src.incbl import incbl
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A incremental bug localization tool")
    parser.add_argument('bug_report_path', help='Bug report path')
    parser.add_argument('code_base_path', help='Codebase directory')
    parser.add_argument('-ft', '--file_type', nargs='+', help='Suffixes of files to be processed', default=['java'])
    args = parser.parse_args()

    bug_report_path = args.bug_report_path
    code_base_path = args.code_base_path
    file_type = args.file_type
    incbl = incbl(bug_report_path, code_base_path, file_type)
    incbl.localization()


