### Constructing vocab files
```
python3 vocab_main.py --train-src <src file> --train-tar <tar file> --size 50000 --freq-cutoff 2 --vocab-file vocab.bin
```
python3 vocab_main.py --train-src data/train.en-az.az.txt --size 50000 --freq-cutoff 2 --vocab-src vocab/en-az.az.bin

python3 generator_main.py --mode greedy --in-file data/test.en-az.en.txt --out-file en-az-res.txt --vocab vocab/en-az.en.bin --n-gram 4 --replace-top 200 --insert-top 100 --displacement-range 3 --replace-prob 0.35 --insert-prob 0.25 --displacement-prob 0.2