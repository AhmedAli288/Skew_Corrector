import cv2
import numpy as np

# This function takes a cv2.imread returned file and returns an image

def skewCorrector(image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  gray = cv2.bitwise_not(gray)
  thresh = cv2.threshold(gray, 0, 255,
    cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
  coords = np.column_stack(np.where(thresh > 0))

  angle = cv2.minAreaRect(coords)[-1]
  h,w = cv2.minAreaRect(coords)[1]

  if h < w:
    angle = (90 - angle)

  else:
    angle = -angle

  (h, w) = image.shape[:2]
  center = (w // 2, h // 2)
  M = cv2.getRotationMatrix2D(center, angle, 1.0)
  rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

  return rotated