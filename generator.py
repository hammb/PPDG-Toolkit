
import trimesh
import pyrender

from PoseUtils import SpecialPoseGenerator

from star.tf.star import STAR
import tensorflow as tf
import numpy as np


def getTrans():
    return tf.constant(np.zeros((1,3)),dtype=tf.float32)

def getBetas():
    betas = np.zeros((1,10))
    betas[0][1] = 3
    return tf.constant(betas,dtype=tf.float32)

def getPoseParameters(angle):
    #["name_of_variation", probabiltiy, max_angle]

    random_variations = [
            ["rotate_head", 1, 0.5, None],
            ["bow_head", 1, 0.5, None],
            ["tilt_head", 1, 0.5, None],
        ]
    
    spg = SpecialPoseGenerator()
    
    spg.from_show_hands_to_stretched_down(angle)
    
    #spg.add_random_variations(random_variations)
    
    return tf.constant(spg.get_pose_parameters(), dtype=tf.float32)
 
def visualize(vertices, joints):

    vertex_colors = np.ones([vertices.shape[0], 4]) * [0.3, 0.3, 0.3, 0.8]
    tri_mesh = trimesh.Trimesh(vertices, faces,
                               vertex_colors=vertex_colors)
    
    export = trimesh.exchange.obj.export_obj(tri_mesh) 
    file_obj = open("model.obj", 'wb') 
    trimesh.util.write_encoded(file_obj, export)

    
    mesh = pyrender.Mesh.from_trimesh(tri_mesh)
    
    scene = pyrender.Scene()
    scene.add(mesh)
    
    sm = trimesh.creation.uv_sphere(radius=0.005)
    sm.visual.vertex_colors = [0.9, 0.1, 0.1, 1.0]
    tfs = np.tile(np.eye(4), (len(joints), 1, 1))
    tfs[:, :3, 3] = joints
    joints_pcl = pyrender.Mesh.from_trimesh(sm, poses=tfs)
    scene.add(joints_pcl)
    
    pyrender.Viewer(scene, use_raymond_lighting=True)     
    
    
batch_size = 10
gender = 'male'
faces = np.load("faces.npy")

star = STAR(gender, batch_size)

trans = getTrans()
betas = getBetas()
pose = getPoseParameters(0)

vertices, joints = star(pose,betas,trans)

vertices = vertices.numpy()[0]
joints = joints.numpy()[0]

visualize(vertices, joints)
