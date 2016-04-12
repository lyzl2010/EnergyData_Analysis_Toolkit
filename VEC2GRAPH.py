from DATA2VEC import *
import matplotlib.pyplot as plt

def vectors2graphs(vectors):
    path = os.path.join(os.getcwd(), RESULT_DIRECTORY, 'graph', 'vectorize', str(VEC_DIMENSION))
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)

    for i in xrange(len(vectors['file_name'])):
        start_time = time.time()

        name = vectors['file_name'][i].rsplit('/', 1)[1]

        print 'drawing graph of VECTORIZED ' + name,

        name = name.split('.')[0]
        name = name + '_vec_' + str(VEC_DIMENSION) + '.jpg'

        x = np.linspace(0, 1, len(vectors['data'][i]))
        plt.scatter(x, vectors['data'][i], marker='+')
        plt.savefig(name)
        plt.close()

        end_time = time.time()

        print '\t\t' + 'run time: ' + str(end_time - start_time)


if __name__ == "__main__":
    start_time = time.time()

    dir_name = get_directory()

    vectors = unpickling(dir_name)

    vectors2graphs(vectors)

    end_time = time.time()

    print '*** TOATL TIME: ' + str(end_time - start_time) + ' ***'
