from pip._vendor import requests
import os
import unittest

class testdownload(unittest.TestCase):
    #10:1
    def download_gh(self,date, hour):
        url = f"https://data.gharchive.org/{date}-{hour:02}.json.gz"
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            print('successful')
            file_name = f"{date}-{hour:02}.json.gz"
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(os.path.abspath(file_name))
            return os.path.abspath(file_name)
        else:
            return None
    #10:2
    def test_download_gh(self):
        date = '2023-03-01'
        hour = 10
        downloaded_file = self.download_gh(date, hour)
        print(downloaded_file)
        assert downloaded_file is not None
        assert os.path.isfile(downloaded_file)

        # Clean up the downloaded file after the test
        if os.path.isfile(downloaded_file):
            os.remove(downloaded_file)

if __name__ == '__main__':
    unittest.main()
