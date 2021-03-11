root_dir = '/content/drive/My Drive/DeepCID/model_cnn'
datafile3 = 'Xscale.npy'

i=0
for (root, dirs, files) in os.walk(root_dir):
    for d in dirs:
        if not d.startswith('.'):
            dir_path = os.path.join(root, d)
            file_path = os.path.join(dir_path, datafile3)
            Xscale = np.load(file_path)
