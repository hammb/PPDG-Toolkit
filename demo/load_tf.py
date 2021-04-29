# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG),
# acting on behalf of its Max Planck Institute for Intelligent Systems and the
# Max Planck Institute for Biological Cybernetics. All rights reserved.
#
# Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG) is holder of all proprietary rights
# on this computer program. You can only use this computer program if you have closed a license agreement
# with MPG or you get the right to use the computer program from someone who is authorized to grant you that right.
# Any use of the computer program without a valid license is prohibited and liable to prosecution.
# Contact: ps-license@tuebingen.mpg.de
#
#
# If you use this code in a research publication please consider citing the following:
#
# STAR: Sparse Trained  Articulated Human Body Regressor <https://arxiv.org/pdf/2008.08535.pdf>
#
#
# Code Developed by:
# Ahmed A. A. Osman

import trimesh
import pyrender

from MyUtils import SpecialPoseGenerator

from star.tf.star import STAR
import tensorflow as tf
import numpy as np
batch_size = 10
gender = 'male'
star = STAR()
trans = tf.constant(np.zeros((1,3)),dtype=tf.float32)

spg = SpecialPoseGenerator()

spg.from_show_hands_to_stretched_down(1)


pose = spg.get_pose_parameters()

betas = np.zeros((1,10))
betas[0][1] = 2

betas = tf.constant(betas,dtype=tf.float32)
star_mesh = np.array(star(pose,betas,trans))
print(star_mesh)

mesh = pyrender.Mesh.from_points(star_mesh[0])
scene = pyrender.Scene()
scene.add(mesh)
pyrender.Viewer(scene, use_raymond_lighting=True)