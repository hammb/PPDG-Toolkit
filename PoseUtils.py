import numpy as np
import tensorflow as tf

class PoseParameterGenerator():
    
    def __init__(self):
        self.pose_parameters = np.zeros((1,72))
         
    def get_pose_parameters(self):
        return tf.constant(self.pose_parameters, dtype=tf.float32)
    
    def set_pose_parameters(self, pose_parameters):
        self.pose_parameters = pose_parameters
    
    def check_arguments(self, direction, angle):
        wrong_direction_argument = direction == 1 or direction == 0
        wrong_angle_argument = angle >= 0 and angle <= 1
        
        if not wrong_direction_argument:
            raise ValueError("Wrong Direction passed. Should be 0 or 1")
        elif not wrong_angle_argument:
            raise ValueError("Wrong Angle passed. Should be between 0 and 1")
            
    
    def rotate_right_hand(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Vorne", Handrücken rotieren zum Betrachter
        direction = 0: Rotation "nach Hinten", Handflächen rotieren zum Betrachter
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.3
            
            self.pose_parameters[0][60] = angle * rotation_factor
            self.pose_parameters[0][66] = angle * rotation_factor
        
        else:
            rotation_factor = -0.5
            
            self.pose_parameters[0][60] = angle * rotation_factor
            self.pose_parameters[0][66] = angle * rotation_factor
    
    def rotate_right_elbow(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Vorne", Handrücken rotieren zum Betrachter
        direction = 0: Rotation "nach Hinten", Handflächen rotieren zum Betrachter
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.6
            
            self.pose_parameters[0][54] = angle * rotation_factor
            
        else:
            rotation_factor = -1.3
            
            self.pose_parameters[0][54] = angle * rotation_factor
        
    def rotate_right_shoulder(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Vorne", Handrücken rotieren zum Betrachter
        direction = 0: Rotation "nach Hinten", Handflächen rotieren zum Betrachter
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.1
            
            self.pose_parameters[0][39] = angle * rotation_factor
            self.pose_parameters[0][48] = angle * rotation_factor
            
        else:
            rotation_factor = -0.45
            
            self.pose_parameters[0][39] = angle * rotation_factor
            self.pose_parameters[0][48] = angle * rotation_factor

        
    def rotate_whole_right_arm(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Vorne", Handrücken rotieren zum Betrachter
        direction = 0: Rotation "nach Hinten", Handflächen rotieren zum Betrachter
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad

        Returns
        -------
        None.

        """
        
        self.rotate_right_shoulder(direction,angle)
        self.rotate_right_elbow(direction,angle)
        self.rotate_right_hand(direction,angle)

    def rotate_left_hand(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Vorne", Handrücken rotieren zum Betrachter
        direction = 0: Rotation "nach Hinten", Handflächen rotieren zum Betrachter
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            
            rotation_factor = 0.3
            
            self.pose_parameters[0][63] = angle * rotation_factor
            self.pose_parameters[0][69] = angle * rotation_factor
        else:
            
            rotation_factor = -0.5
            
            self.pose_parameters[0][63] = angle * rotation_factor
            self.pose_parameters[0][69] = angle * rotation_factor

    def rotate_left_elbow(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Vorne", Handrücken rotieren zum Betrachter
        direction = 0: Rotation "nach Hinten", Handflächen rotieren zum Betrachter
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.6
            
            self.pose_parameters[0][57] = angle * rotation_factor
            
        else:
            rotation_factor = -1.3
            
            self.pose_parameters[0][57] = angle * rotation_factor

    def rotate_left_shoulder(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Vorne", Handrücken rotieren zum Betrachter
        direction = 0: Rotation "nach Hinten", Handflächen rotieren zum Betrachter
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.1
            
            self.pose_parameters[0][42] = angle * rotation_factor
            self.pose_parameters[0][51] = angle * rotation_factor
            
        else:
            rotation_factor = -0.45
            
            self.pose_parameters[0][42] = angle * rotation_factor
            self.pose_parameters[0][51] = angle * rotation_factor

    def rotate_whole_left_arm(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Vorne", Handrücken rotieren zum Betrachter
        direction = 0: Rotation "nach Hinten", Handflächen rotieren zum Betrachter
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.rotate_left_shoulder(direction,angle)
        self.rotate_left_elbow(direction,angle)
        self.rotate_left_hand(direction,angle)

    def lift_or_lower_right_arm(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Oben", Hebt den Arm (Rotation um Schulter) nach oben
        direction = 0: Rotation "nach Unten", Senkt den Arm (Rotation um Schulter) nach unten
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad

        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            
            rotation_factor = 0.75
            
            self.pose_parameters[0][41] = rotation_factor * angle
            self.pose_parameters[0][50] = rotation_factor * angle
            
        if direction == 0:
        
            rotation_factor = -0.6
            
            self.pose_parameters[0][41] = rotation_factor * angle
            self.pose_parameters[0][50] = rotation_factor * angle
            
    
    def lift_or_lower_left_arm(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Oben", Hebt den Arm (Rotation um Schulter) nach oben
        direction = 0: Rotation "nach Unten", Senkt den Arm (Rotation um Schulter) nach unten
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad

        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = -0.75
            
            self.pose_parameters[0][44] = rotation_factor * angle
            self.pose_parameters[0][53] = rotation_factor * angle
            
        if direction == 0:
            rotation_factor = 0.6
            
            self.pose_parameters[0][44] = rotation_factor * angle
            self.pose_parameters[0][53] = rotation_factor * angle
            
    def bow_right_elbow_to_front(self, angle = 1):
        """
        

        Parameters
        ----------
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
            
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(0 , angle) #There is only one direction, so no direction argument
        
        rotation_factor = -2
        self.pose_parameters[0][56] = rotation_factor * angle
        
    def bow_left_elbow_to_front(self, angle = 1):
        """
        

        Parameters
        ----------
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad        

        Returns
        -------
        None.

        """
        
        self.check_arguments(0 , angle) #There is only one direction, so no direction argument
        
        rotation_factor = 2
        self.pose_parameters[0][59] = rotation_factor * angle
        
    def bow_right_elbow_to_back(self, angle = 1):
        """
        

        Parameters
        ----------
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
            
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(0 , angle) #There is only one direction, so no direction argument
        
        rotation_factor = 2
        self.pose_parameters[0][56] = rotation_factor * angle
        
    def bow_left_elbow_to_back(self, angle = 1):
        """
        

        Parameters
        ----------
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad        

        Returns
        -------
        None.

        """
        
        self.check_arguments(0 , angle) #There is only one direction, so no direction argument
        
        rotation_factor = -2
        self.pose_parameters[0][59] = rotation_factor * angle
        
    def bow_left_elbow_to_top(self, angle = 1):
        """
        

        Parameters
        ----------
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad        

        Returns
        -------
        None.

        """
        
        self.check_arguments(0 , angle) #There is only one direction, so no direction argument
        
        rotation_factor = 2
        self.pose_parameters[0][58] = rotation_factor * angle
        
    def bow_left_elbow_to_bottom(self, angle = 1):
        """
        

        Parameters
        ----------
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad        

        Returns
        -------
        None.

        """
        
        self.check_arguments(0 , angle) #There is only one direction, so no direction argument
        
        rotation_factor = -2
        self.pose_parameters[0][58] = rotation_factor * angle
        
    def bow_right_elbow_to_top(self, angle = 1):
        """
        

        Parameters
        ----------
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
            
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(0 , angle) #There is only one direction, so no direction argument
        
        rotation_factor = -2
        self.pose_parameters[0][55] = rotation_factor * angle
        
    def bow_right_elbow_to_bottom(self, angle = 1):
        """
        

        Parameters
        ----------
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
            
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(0 , angle) #There is only one direction, so no direction argument
        
        rotation_factor = 2
        self.pose_parameters[0][55] = rotation_factor * angle
        
    def lift_or_lower_right_leg_front_or_back(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Vorne", Hebt das Bein vorne nach oben
        direction = 0: Rotation "nach Hinten", Hebt das Bein hinten nach oben
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 1.6
            
            self.pose_parameters[0][3] = rotation_factor * angle
        
        else:
            rotation_factor = -1.6
            
            self.pose_parameters[0][3] = rotation_factor * angle
            
    def lift_or_lower_left_leg_front_or_back(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "nach Vorne", Hebt das Bein vorne nach oben
        direction = 0: Rotation "nach Hinten", Hebt das Bein hinten nach oben
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 1.6
            
            self.pose_parameters[0][6] = rotation_factor * angle
        
        else:
            rotation_factor = -1.6
            
            self.pose_parameters[0][6] = rotation_factor * angle
    
    def lift_or_lower_right_leg_sideways(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "Zur Seite hoch", Hebt das Bein seitlich nach oben
        direction = 0: Rotation "nach Innen", Senkt das Bein zum anderen Bein
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 1.6
            
            self.pose_parameters[0][5] = rotation_factor * angle
        
        else:
            rotation_factor = -0.1
            
            self.pose_parameters[0][5] = rotation_factor * angle
            
    def lift_or_lower_left_leg_sideways(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "Zur Seite hoch", Hebt das Bein seitlich nach oben
        direction = 0: Rotation "nach Innen", Senkt das Bein zum anderen Bein
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = -1.6
            
            self.pose_parameters[0][8] = rotation_factor * angle
        
        else:
            rotation_factor = 0.1
            
            self.pose_parameters[0][8] = rotation_factor * angle
        
    def bow_right_knee(self, angle = 1):
        """
        

        Parameters
        ----------
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad        

        Returns
        -------
        None.

        """
        
        self.check_arguments(0 , angle) #There is only one direction, so no direction argument
        
        rotation_factor = 2
        self.pose_parameters[0][12] = rotation_factor * angle
        
    def bow_left_knee(self, angle = 1):
        """
        

        Parameters
        ----------
        angle : TYPE, optional
            DESCRIPTION. The default is 1.

        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad        

        Returns
        -------
        None.

        """
        
        self.check_arguments(0 , angle) #There is only one direction, so no direction argument
        
        rotation_factor = 2
        self.pose_parameters[0][15] = rotation_factor * angle
        
    
    def rotate_left_hip(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "Nach Innen", Bein dreht sich zum anderen Bein hin
        direction = 0: Rotation "Nach Aussen", Bein dreht sich Aussen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.3
            
            self.pose_parameters[0][7] = angle * rotation_factor
            
        else:
            rotation_factor = -0.35
            
            self.pose_parameters[0][7] = angle * rotation_factor
            
    def rotate_right_hip(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "Nach Innen", Bein dreht sich zum anderen Bein hin
        direction = 0: Rotation "Nach Aussen", Bein dreht sich Aussen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = -0.3
            
            self.pose_parameters[0][4] = angle * rotation_factor
            
        else:
            rotation_factor = 0.35
            
            self.pose_parameters[0][4] = angle * rotation_factor
            
    def rotate_left_knee(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "Nach Innen", Bein dreht sich zum anderen Bein hin
        direction = 0: Rotation "Nach Aussen", Bein dreht sich Aussen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.3
            
            self.pose_parameters[0][16] = angle * rotation_factor
            
        else:
            rotation_factor = -0.35
            
            self.pose_parameters[0][16] = angle * rotation_factor
            
    def rotate_right_knee(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "Nach Innen", Bein dreht sich zum anderen Bein hin
        direction = 0: Rotation "Nach Aussen", Bein dreht sich Aussen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = -0.3
            
            self.pose_parameters[0][13] = angle * rotation_factor
            
        else:
            rotation_factor = 0.35
            
            self.pose_parameters[0][13] = angle * rotation_factor
            
    def rotate_left_foot(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "Nach Innen", Bein dreht sich zum anderen Bein hin
        direction = 0: Rotation "Nach Aussen", Bein dreht sich Aussen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.3
            
            self.pose_parameters[0][25] = angle * rotation_factor
            
        else:
            rotation_factor = -0.35
            
            self.pose_parameters[0][25] = angle * rotation_factor
            
    def rotate_right_foot(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "Nach Innen", Bein dreht sich zum anderen Bein hin
        direction = 0: Rotation "Nach Aussen", Bein dreht sich Aussen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = -0.3
            
            self.pose_parameters[0][22] = angle * rotation_factor
            
        else:
            rotation_factor = 0.35
            
            self.pose_parameters[0][22] = angle * rotation_factor
            
    def rotate_right_leg(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "Nach Innen", Bein dreht sich zum anderen Bein hin
        direction = 0: Rotation "Nach Aussen", Bein dreht sich Aussen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.rotate_right_hip(direction, angle)
        self.rotate_right_knee(direction, angle)
        self.rotate_right_foot(direction, angle)
        
    def rotate_left_leg(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rotation "Nach Innen", Bein dreht sich zum anderen Bein hin
        direction = 0: Rotation "Nach Aussen", Bein dreht sich Aussen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.rotate_left_hip(direction, angle)
        self.rotate_left_knee(direction, angle)
        self.rotate_left_foot(direction, angle)
        
    def bend_over_and_back(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Rücken nach vorne bücken
        direction = 0: Rücken nach hinten bücken
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.6
            
            self.pose_parameters[0][9] = angle * rotation_factor
            self.pose_parameters[0][18] = angle * rotation_factor
            self.pose_parameters[0][27] = angle * rotation_factor
            
        else:
            rotation_factor = - 0.35
            
            self.pose_parameters[0][9] = angle * rotation_factor
            self.pose_parameters[0][18] = angle * rotation_factor
            self.pose_parameters[0][27] = angle * rotation_factor
    
    def rotate_torso(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Torso nach rechts drehen (Gesicht schaut nach rechts)
        direction = 0: Torso nach links drehen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.6
            
            self.pose_parameters[0][10] = angle * rotation_factor
            self.pose_parameters[0][19] = angle * rotation_factor
            self.pose_parameters[0][28] = angle * rotation_factor
            
        else:
            rotation_factor = - 0.6
            
            self.pose_parameters[0][10] = angle * rotation_factor
            self.pose_parameters[0][19] = angle * rotation_factor
            self.pose_parameters[0][28] = angle * rotation_factor
            
    def tilt_torso(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Torso nach rechts neigen
        direction = 0: Torso nach links neigen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.4
            
            self.pose_parameters[0][11] = angle * rotation_factor
            self.pose_parameters[0][20] = angle * rotation_factor
            self.pose_parameters[0][29] = angle * rotation_factor
            
        else:
            rotation_factor = - 0.4
            
            self.pose_parameters[0][11] = angle * rotation_factor
            self.pose_parameters[0][20] = angle * rotation_factor
            self.pose_parameters[0][29] = angle * rotation_factor
            
    def tilt_head(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Kopf nach rechts neigen
        direction = 0: Kopf nach links neigen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = - 0.6
            
            self.pose_parameters[0][38] = angle * rotation_factor
            self.pose_parameters[0][47] = angle * rotation_factor
            
            
        else:
            rotation_factor = 0.6
            
            self.pose_parameters[0][38] = angle * rotation_factor
            self.pose_parameters[0][47] = angle * rotation_factor
            
    def rotate_head(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Kopf nach rechts drehen
        direction = 0: Kopf nach links drehen
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 1
            
            self.pose_parameters[0][37] = angle * rotation_factor
            self.pose_parameters[0][46] = angle * rotation_factor
            
            
        else:
            rotation_factor = - 1
            
            self.pose_parameters[0][37] = angle * rotation_factor
            self.pose_parameters[0][46] = angle * rotation_factor
            
    def bow_head(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Kopf nach vorne senken
        direction = 0: Kopf nach hinten senken
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 0.6
            
            self.pose_parameters[0][36] = angle * rotation_factor
            self.pose_parameters[0][45] = angle * rotation_factor
            
            
        else:
            rotation_factor = - 0.6
            
            self.pose_parameters[0][36] = angle * rotation_factor
            self.pose_parameters[0][45] = angle * rotation_factor
            
    def rotate_right_arm_horizontally_to_front(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Arm (an Schulter) horizontal bewegen nach vorne
        direction = 0: Arm (an Schulter) horizontal bewegen nach hinten
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = -1
            
            self.pose_parameters[0][40] = angle * rotation_factor
            self.pose_parameters[0][49] = angle * rotation_factor
            
        else:
            rotation_factor = 0.2
            
            self.pose_parameters[0][40] = angle * rotation_factor
            self.pose_parameters[0][49] = angle * rotation_factor
            
    def rotate_left_arm_horizontally_to_front(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Perspektive ausgehend von T-Pose. Man betrachtet das Modell von Vorne (Also sieht Gesicht, Bauch, etc.)
        
        direction = 1: Arm (an Schulter) horizontal bewegen nach vorne
        direction = 0: Arm (an Schulter) horizontal bewegen nach hinten
        
        angle = 0: Keine Rotation
        angle = 1: Maximale Rotation
        
        rotation_factor: ~1.6 = 90 Grad
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        if direction == 1:
            rotation_factor = 1
            
            self.pose_parameters[0][43] = angle * rotation_factor
            self.pose_parameters[0][52] = angle * rotation_factor
            
        else:
            rotation_factor = -0.2
            
            self.pose_parameters[0][43] = angle * rotation_factor
            self.pose_parameters[0][52] = angle * rotation_factor
            
            
class SpecialPoseGenerator(PoseParameterGenerator):
    
    def __init__(self, *args, **kwargs):
        super(SpecialPoseGenerator, self).__init__(*args, **kwargs)
    
    def lift_one_arm_and_press_other_to_body(self, direction = 1, angle = 1, arm = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        arm : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Ein Arm ist seitlich am Körper angelegt. Der andere ist ausgestreckt und kann seitlich von "ausgestreckt nach oben" bis 
        "ausgestreckt nach unten" rotieren.
        
        Raises
        ------
        ValueError
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        wrong_arm_argument = arm == 0 or arm == 1
        
        if not wrong_arm_argument:
            raise ValueError("Wrong Arm passed. Should be 0 or 1")
            
        if arm == 1:
            
            self.lift_or_lower_left_arm(0, 1) # Press left arm to body
            self.lift_or_lower_right_arm(direction, angle) 
            
        else:
            
            self.lift_or_lower_right_arm(0, 1) # Press right arm to body
            self.lift_or_lower_left_arm(direction, angle) 
            
    def lift_one_arm_and_lift_and_fix_other(self, direction = 1, angle = 1, arm = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        arm : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Ein Arm ist nach oben ausgestreckt. Der andere ist ausgestreckt und kann seitlich von "ausgestreckt nach oben" bis 
        "ausgestreckt nach unten" rotieren.
        
        Raises
        ------
        ValueError
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        wrong_arm_argument = arm == 0 or arm == 1
        
        if not wrong_arm_argument:
            raise ValueError("Wrong Arm passed. Should be 0 or 1")
            
        if arm == 1:
            
            self.lift_or_lower_left_arm(1, 1) # Lift left arm
            self.lift_or_lower_right_arm(direction, angle) 
            
        else:
            
            self.lift_or_lower_right_arm(1, 1) # Lift right arm
            self.lift_or_lower_left_arm(direction, angle)
            
    def lift_arms_symmetrically(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Beide Arme bewegen sich symmetrisch von "unten ausgestreckt" bis "oben ausgestreckt"
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        self.lift_or_lower_left_arm(direction, angle) 
        self.lift_or_lower_right_arm(direction, angle) 
        
    def lift_arms_contrarily(self, direction = 1, angle = 1):
        """
        

        Parameters
        ----------
        direction : TYPE, optional
            DESCRIPTION. The default is 1.
        angle : TYPE, optional
            DESCRIPTION. The default is 1.
        
        Beide arme bewegen sich konträr zu einander. Wenn der eine durch gestreckt ist, ist der andere angezogen
        
        Returns
        -------
        None.

        """
        
        self.check_arguments(direction, angle)
        
        self.lift_or_lower_left_arm(direction, angle)
        
        dif = [1, 0]
        self.lift_or_lower_right_arm(dif[direction], angle)
    
    def show_hands(self):
        """
        Statisch: Hände hoch, Ellenbogen um 90 grad gekümmt, Handflächen zeigen nach vorne.

        Returns
        -------
        None.

        """
        
        
        self.rotate_left_shoulder(0, 1)
        self.rotate_left_elbow(0, 0.5)
        self.bow_left_elbow_to_top(0.9)
        self.rotate_left_hand(1, 0.7)
        
        self.rotate_right_shoulder(0, 1)
        self.rotate_right_elbow(0, 0.5)
        self.bow_right_elbow_to_top(0.9)
        self.rotate_right_hand(1, 0.7)
        
    def from_show_hands_to_stretched_up(self, angle):
        
        self.rotate_left_shoulder(0, 1)
        self.rotate_left_elbow(0, 0.5)
        self.bow_left_elbow_to_top(0.9 - (angle * 0.9))
        self.rotate_left_hand(1, 0.7)
        
        self.rotate_right_shoulder(0, 1)
        self.rotate_right_elbow(0, 0.5)
        self.bow_right_elbow_to_top(0.9 - (angle * 0.9))
        self.rotate_right_hand(1, 0.7)
        
        self.lift_arms_symmetrically(1, angle)
        
        self.rotate_left_arm_horizontally_to_front(1, angle * 0.3)  
        self.rotate_right_arm_horizontally_to_front(1, angle * 0.3) 
        
    def from_show_hands_to_stretched_down(self, angle):
        
        self.rotate_left_shoulder(0, 1)
        self.rotate_left_elbow(0, 0.5)
        self.bow_left_elbow_to_top(0.9 - (angle * 0.9))
        self.rotate_left_hand(1, 0.7)
        
        self.rotate_right_shoulder(0, 1)
        self.rotate_right_elbow(0, 0.5)
        self.bow_right_elbow_to_top(0.9 - (angle * 0.9))
        self.rotate_right_hand(1, 0.7)
        
        self.lift_arms_symmetrically(0, angle)
        
        self.rotate_left_arm_horizontally_to_front(0, angle * 0.4)  
        self.rotate_right_arm_horizontally_to_front(0, angle * 0.4) 


"""
Perspektive T-Pose zum Betrachter hin gerichtet

#body_pose[0][3] = -1.6 rechtes Bein 90 Grad nach vorne gestreckt (+- 1.6)
#body_pose[0][4] = -1.6 rechte Hüfte 90 Grad nach innen gedreht (UNREALISTISCH) + - 0.35 realistisch
#body_pose[0][5] = 1.6  rechtes Bein 90 Grad nach aussen gestreckt (+- 1.6)

#body_pose[0][6] = -1.6 linkes Bein 90 Grad nach vorne gestreckt (+- 1.6)
#body_pose[0][7] = 1.6  linke Hüfte 90 Grad nach innen gedreht (UNREALISTISCH) + - 0.35 realistisch
#body_pose[0][8] = -1.6 linkes Bein 90 Grad nach aussen gestreckt (-1.6 - 0.1)

#body_pose[0][9] = 1.6 Oberkörper 90 Grad nach vorne gebeugt (-0.5 - 1.6)
#body_pose[0][10] = 1.6 Oberkörper 90 Grad nach rechts gedreht (+- 0.6)
#body_pose[0][11] = 1.6 Oberkörper 90 Grad nach links geneigt (+- 0.6)

#body_pose[0][12] = 1.6 rechtes Knie um 90 Grad gebeugt (0 - 1.6)
#body_pose[0][13] = 1.6 Um das rechte Knie um 90 Grad nach aussen gedreht (+-0.35)
-body_pose[0][14] = 1.6 Rechtes Knie um 90 grad nach aussen geklappt (UNREALISTISCH) (+ - 0.1) realistisch

#body_pose[0][15] = 1.6 linkes Knie um 90 Grad gebeugt (0 - 1.6)
#body_pose[0][16] = 1.6 Um das linke Knie 90 Grad nach innen gedreht (+- 0.35) 
-body_pose[0][17] = -1.6 Das linke Knie um 90 Grad nach aussen geklappt (UNREALISTISCH) (+ - 0.1) realistisch

#body_pose[0][18] = 1.6 Oberkörper am Oberen Rücken 90 Grad nach vorne gebeugt, großer Buckel (- 0.5 - 0.6) realistisch
#body_pose[0][19] = -1.6 Oberkörper auf Bauchhöhe 90 Grad nach links gedreht (+- 0.6)
#body_pose[0][20] = -1.6 Oberkörper auf Bauch Höhe 90 Grad nach rechts geklappt (UNREALISTISCH) + - 0.6 realistisch

body_pose[0][21] = 1.6 Rechter Fuß durchgestreckt nach unten (-0.5 - 1) 
#body_pose[0][22] = 1.6 Rechter Fuß um 90 Grad nach aussen gedreht (+ - 0.35)
body_pose[0][23] = 1.6 Rechter fuß um 90 Grad nach aussen gekalppt (Unrealistisch) (-0.5 - 0.2)

body_pose[0][24] = 1.6 Linker Fuß durchgestreckt nach unten (-0.5 - 1) 
#body_pose[0][25] = 1.6 Linker Fuß um 90 Grad nach innen gedreht (+ - 0.35)
body_pose[0][26] = 1.6 Linker fuß um 90 Grad nach innen gekalppt (Unrealistisch) (0.2 - 0.5)

#body_pose[0][27] = 1.6 Oberkörper am Oberen Rücken 90 Grad nach vorne gebeugt, großer Buckel (- 0.5 - 0.6) realistisch
#body_pose[0][28] = 1.6 Oberkörper auf Brust höhe 90 Grad nach rechts gedreht (+- 0.6)
#body_pose[0][29] = 1.6 Oberkörper auf Brust höhe 90 Grad nach links geklappt (+- 0.6)

body_pose[0][30] = 1.6 Rechte Fuß Zehen um 90 Grad nach unten gekalppt(+- 0.7)
-body_pose[0][31] = 1.6 Rechte Fuß Zehen um 90 Grad nach aussen Rotiert (+- 0.1)
-body_pose[0][32] = 1.6 Rechte Fuß Zehen um 90 Grad nach aussen Rotiert (+- 0.1)

body_pose[0][33] = 1.6 Linke Fuß Zehen um 90 Grad nach unten gekalppt(+- 0.7)
-body_pose[0][34] = 1.6 Linke Fuß Zehen um 90 Grad nach innen Rotiert (+- 0.1)
-body_pose[0][35] = 1.6 Linke Fuß Zehen um 90 Grad nach innen Rotiert (+- 0.1)

#body_pose[0][36] = 1.6 Kopf um nacken um 90 grad nach vorne rotiert (+ - 0.6)!
#body_pose[0][37] = 1.6 Kopf um nacken um 90 grad nach rechts gedreht (+ - 0.6)!
#body_pose[0][38] = 1.6 Kopf um nacken um 90 grad nach links geklappt (+ - 0.6)!

#body_pose[0][39] = 1.6 Rechte Schulter um 90 grad rotiert, Handrücken zeigt nach vorne (+- 0.1)
#body_pose[0][40] = -2 Arm um Rechte Schulter nach vorne Rotiert zeigt schräg nach vorne (-1 - 0.15) 
#body_pose[0][41] = 1.6 Arm um Rechte schulter nach oben Durchgestreckt (-+ 0.6)

#body_pose[0][42] = 1.6 Linke Schulter um 90 grad rotiert, Handrücken zeigt nach vorne (+- 0.1)
#body_pose[0][43] = 2 Arm um Linke Schulter nach vorne Rotiert zeigt schräg nach vorne (-0.15 - 1)
#body_pose[0][44] = 1.6 Arm um Linke schulter nach unten Durchgestreckt (+- 0.6)

#body_pose[0][45] = 1.6 Kopf um oberen nacken um 90 grad nach vorne rotiert (+ - 0.6)!
#body_pose[0][46] = 1.6 Kopf um oberen nacken um 90 grad nach rechts gedreht (+ - 0.6)!
#body_pose[0][47] = 1.6 Kopf um oberen nacken um 90 grad nach links geklappt (+ - 0.6)!

#body_pose[0][48] = 1.6 Rechte Schulter um 90 grad rotiert, Handrücken zeigt nach vorne (+- 0.1)
#body_pose[0][49] = -2 Arm um Rechte Schulter nach vorne Rotiert zeigt schräg nach vorne (-1 - 0.15)
#body_pose[0][50] = 1.6 Arm um Rechte schulter nach oben Durchgestreckt (-+ 0.6)

#body_pose[0][51] = 1.6 Linke Schulter um 90 grad rotiert, Handrücken zeigt nach vorne (+- 0.1)
#body_pose[0][52] = 2 Arm um Linke Schulter nach vorne Rotiert zeigt schräg nach vorne (-0.15 - 1)
#body_pose[0][53] = 1.6 Arm um Linke schulter nach unten Durchgestreckt (-+ 0.6)

#body_pose[0][54] = 1.6 Rechter Arm um Ellenbogen 90 Grad rotiert. Handflächen zeigen nach vorne (+-0.6)
-body_pose[0][55] = 1.6 Rechter Arm um Ellenbogen 90 Grad nach hinten geklappt (UNREALISTISCH) (+ - 0.1)
#body_pose[0][56] = - 1.6 Rechter Arm um Ellenbogen 90 Grad gebeugt (-1.6 - 0)

#body_pose[0][57] = 1.6 Linker Arm um Ellenbogen 90 Grad rotiert. Handflächen zeigen nach vorne (+-0.6)
-body_pose[0][58] = 1.6 Rechter Arm um Ellenbogen 90 Grad nach hinten geklappt (UNREALISTISCH) (+ - 0.1)
#body_pose[0][59] = - 1.6 Rechter Arm um Ellenbogen 90 Grad gebeugt (0 - 1.6)

#body_pose[0][60] = 1.6 Rechte Hand um 90 Grad rotiert. Handflächen zeigen nach vorne (+-0.3)
body_pose[0][61] = 1.6 Rechte Hand 90 Grad nach hinten geklappt (+ - 0.5)
body_pose[0][62] = - 1.6 Rechte Hand nach vorne gebeugt (+-0.8)

#body_pose[0][63] = 1.6 Linke Hand um 90 Grad rotiert. Handflächen zeigen nach vorne (+-0.6)
body_pose[0][64] = 1.6 Linke Hand 90 Grad nach vorne geklappt (+ - 1.0)
body_pose[0][65] = 1.6 Linke Hand nach vorne gebeugt (+-1.6)

#body_pose[0][66] = 1.6 Rechte Hand um 90 Grad rotiert. Handflächen zeigen nach vorne (+-0.3)
body_pose[0][67] = 1.6 Rechte Hand 90 Grad nach hinten geklappt (+ - 0.5)
body_pose[0][68] = - 1.6 Rechte Hand nach vorne gebeugt (+-0.8)

#body_pose[0][69] = 1.6 Linke Hand um 90 Grad rotiert. Handflächen zeigen nach vorne (+-0.3)
body_pose[0][70] = 1.6 Linke Hand 90 Grad nach vorne geklappt (+ - 0.5)
body_pose[0][71] = 1.6 Linke Hand nach vorne gebeugt (+-0.8)
"""

