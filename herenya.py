from deepface import DeepFace
import cv2
import json
from glob import glob

def face_analyze(path):
    try:
        result_dict = DeepFace.analyze(
            #img_path='faces/harry.jpg', actions=['age', 'gender', 'race', 'emotion'])
            img_path=path, actions=['age', 'gender', 'race', 'emotion'])

        with open('face_analyze.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        print(f'[+] Age: {result_dict.get("age")}')
        print(f'[+] Gender: {result_dict.get("gender")}')
        print('[+] Race:')

        for k, v in result_dict.get('race').items():
            print(f'{k} - {round(v, 2)}%')

        print('[+] Emotions:')

        for k, v in result_dict.get('emotion').items():
            print(f'{k} - {round(v, 2)}%')

        return result_dict

    except Exception as _ex:
        return _ex

def many_face_analyze(imgs):
    try:
        for img in imgs:
            cv2.imread(img)
            result_dict = DeepFace.analyze(
                #img_path='faces/harry.jpg', actions=['age', 'gender', 'race', 'emotion'])
                img_path=img, actions=['age', 'gender', 'race', 'emotion'])

            with open('face_analyze.json', 'w') as file:
                json.dump(result_dict, file, indent=4, ensure_ascii=False)

            for k, v in result_dict.get('emotion').items():
                print(f'{k} - {round(v, 2)}%')

        # return result_dict

    except Exception as _ex:
        return _ex

if __name__ == '__main__':
    face_analyze('faces/snoop.jpg')
    # imgs = glob("faces/*")
    # many_face_analyze(imgs)
