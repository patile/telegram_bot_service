import requests, json


class Photo2Down:
    def __init__(self, TOKEN):
        self.TOKEN = TOKEN

    def download_and_save(self, file_id,file_name):

        file_meta_data = requests.get("https://api.telegram.org/bot{}/getFile?file_id={}".format(self.TOKEN,
                                                                                                 file_id))  ## resme ait meta data boyut,path vs
        tmp_file_meta_data = json.loads(file_meta_data.content)  # converting

        if tmp_file_meta_data['ok'] == True:  ##resim id status contorl
            file_path = tmp_file_meta_data['result']['file_path']  ## file path

            file_data = requests.get(
                "https://api.telegram.org/file/bot{}/{}".format(self.TOKEN, file_path))  ##isterk ve gelen binary data

            if file_data.status_code != 200:
                return "ERROR Code {}".format(file_data.status_code)
            else:
                self.create_jpeg(file_data.content, file_name=file_name)  ## bu binary dosyaya yazılıyor.



    def create_jpeg(self, binary_content,file_name):
        file = open("{}".format(file_name), "wb")
        file.write(binary_content)
        file.close()

