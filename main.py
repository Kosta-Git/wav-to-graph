from wav_reader import wav
from matplotlib import pyplot as plt


if __name__ == '__main__':
    start, end = 0, 200

    reader = wav.Wav('test.wav')
    reader.read()
    print(reader.get_bytes())

    plt.title("Wav bytes")
    plt.xlabel("time")
    plt.ylabel("value")

    plt.plot(reader.get_bytes()[start:end])
    plt.show()
