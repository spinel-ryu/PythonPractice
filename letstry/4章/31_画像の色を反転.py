import sys
import cv2

if len(sys.argv)<2:
    print('表示したいファイル名を指定してください。')
    sys.exit()

file = sys.argv[1]

try:
    img = cv2.imread(file)

    if img is None:
        raise ValueError('ファイルが見つかりません。')

    negaposi = cv2.bitwise_not(img)

    cv2.imshow(file, negaposi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()
