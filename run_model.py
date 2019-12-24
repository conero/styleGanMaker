# Thanks to StyleGAN provider —— Copyright (c) 2019, NVIDIA CORPORATION.
#
# This work is trained by Copyright(c) 2018, seeprettyface.com, BUPT_GWY.

"""Minimal script for generating an image using pre-trained StyleGAN generator."""

import os
import pickle
import numpy as np
import PIL.Image
import dnnlib.tflib as tflib

synthesis_kwargs = dict(output_transform=dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True), minibatch_size=8)


def text_save(file, data):  # save generate code, which can be modified to generate customized style
    for i in range(len(data[0])):
        s = str(data[0][i]) + '\n'
        file.write(s)


def main():
    # Initialize TensorFlow.
    tflib.init_tf()

    # Load pre-trained network.
    model_path = 'model/generator_asian_star.pkl'

    # Prepare result folder
    result_dir = 'result'
    os.makedirs(result_dir, exist_ok=True)
    os.makedirs(result_dir + '/generate_code', exist_ok=True)

    with open(model_path, "rb") as f:
        _G, _D, Gs = pickle.load(f, encoding='latin1')

    # Print network details.
    Gs.print_layers()

    # Generate pictures
    generate_num = 20
    for i in range(generate_num):
        # Generate latent.
        latents = np.random.randn(1, Gs.input_shape[1])

        # Save latent.
        txt_filename = os.path.join(result_dir, 'generate_code/' + str(i).zfill(4) + '.txt')
        file = open(txt_filename, 'w')
        text_save(file, latents)

        # Generate image.
        fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
        images = Gs.run(latents, None, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)

        # Save image.
        png_filename = os.path.join(result_dir, str(i).zfill(4) + '.png')
        PIL.Image.fromarray(images[0], 'RGB').save(png_filename)

        # Close file.
        file.close()


def execute_model(model_path, **params):
    """
    模型运行
    :param model_path: 模型路劲
    :param params:      可选参数 {out-dir, num}
    :return:
    """
    # Initialize TensorFlow.
    tflib.init_tf()

    # Load pre-trained network.
    # Prepare result folder
    result_dir = './output/'

    if 'out-dir' in params:
        result_dir += params['out-dir']
    else:
        result_dir += os.path.basename(result_dir)

    os.makedirs(result_dir, exist_ok=True)
    os.makedirs(result_dir + '/generate_code', exist_ok=True)

    with open(model_path, "rb") as f:
        _G, _D, Gs = pickle.load(f, encoding='latin1')

    # Print network details.
    Gs.print_layers()

    # Generate pictures
    generate_num = 20
    if 'num' in params:
        generate_num = int(params['num'])

    for i in range(generate_num):
        # Generate latent.
        latents = np.random.randn(1, Gs.input_shape[1])

        # Save latent.
        txt_filename = os.path.join(result_dir, 'generate_code/' + str(i).zfill(4) + '.txt')
        file = open(txt_filename, 'w')
        text_save(file, latents)

        # Generate image.
        fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
        images = Gs.run(latents, None, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)

        # Save image.
        png_filename = os.path.join(result_dir, str(i).zfill(4) + '.png')
        PIL.Image.fromarray(images[0], 'RGB').save(png_filename)

        # Close file.
        file.close()


if __name__ == "__main__":
    # @todo 保留原始，暂时
    main()
