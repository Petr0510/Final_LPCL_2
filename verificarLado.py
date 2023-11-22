import cv2
import mediapipe as mp
import numpy as np

def ppal():
    verif = True
    #Variable de la malla facial
    mp_face_mesh= mp.solutions.face_mesh

    face_mesh = mp_face_mesh.FaceMesh(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)

    #Abrir la cámara web
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,260) 
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,220)
    
    while cap.isOpened():
        success,image = cap.read() 
        if image is not None:
            


            # #voltear la imagen para que no se vea al revés y cambiar metodos de color
            # image = cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
            image = cv2.flip(image,1)
            #para mejorar el rendimiento
            image.flags.writeable=False

            #Obtener el resultado de la imagen procesada
            results = face_mesh.process(image)

            #para mejorar el rendimiento
            image.flags.writeable = True
            
            # #restaurar los métodos de color
            # image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

            img_h, img_w, img_c = image.shape
            face_3d=[]
            face_2d=[]
            
            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    for idx, lm in enumerate(face_landmarks.landmark):
                        if idx==33 or idx==263 or id==1 or idx ==61 or idx ==291 or idx ==199:
                            if idx==1:
                                nose_2d = (lm.x*img_w,lm.y*img_h)
                                nose_3d = (lm.x*img_w,lm.y*img_h.lm.z*3000)

                            x, y = int(lm.x*img_w),int(lm.y*img_h)
                            
                            #obtener las coordenadas 2d
                            face_2d.append([x,y])

                            #obtener las coordenadas 3d
                            face_3d.append([x,y,lm.z])

                                #Convertir a vector numpy
                    face_2d =np.array(face_2d,dtype=np.float64)
                    face_3d =np.array(face_3d,dtype=np.float64)

                    #La matriz de la cámara
                    focal_length= 1*img_w
                    
                    cam_matrix = np.array([[focal_length,0,img_h/2],
                                            [0,focal_length,img_w/2],
                                            [0,0,1]])
                    
                    #parámetros de distorsión
                    dist_matrix = np.zeros((4,1),dtype=np.float64)

                    #solucionar PnP
                    success,rot_vec,trans_vec = cv2.solvePnP(face_3d,face_2d,cam_matrix,dist_matrix)

                    #obtener matriz rotacional
                    rmat,jac = cv2.Rodrigues(rot_vec)

                    #Obtener angulos
                    angles,mtx,mtxQ,Qx,Qy,Qz=cv2.RQDecomp3x3(rmat)

                    #obtener la rotación de y
                    x = angles[0]*360
                    y = angles[1]*360
                    z = angles[2]*360
                    
                    
                    # Obtener dirección de la cabeza

                    if y<-8:
                        text,index = "Izquierda",3
                    elif y>8:
                        text ,index= "Derecha",4
                    elif x<-8:
                        text,index = "Abajo",2
                    elif x>8:
                        text ,index= "Arriba",1
                    
                    else:
                        text = "De frente"

                    
                    if verif == True and text!="De frente":
                        verif = False
                        cap.release()
                        cv2.destroyAllWindows()
                        return index
                    

                    
                    
            
            cv2.imshow("Mi video",image)
                #cerrar con q
            if cv2.waitKey(100)==ord("q"):
                break
        else:
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH,260) 
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT,220)
            success,image = cap.read()
            if image is not None:
               cv2.imshow("Mi video",image) 
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    ppal()