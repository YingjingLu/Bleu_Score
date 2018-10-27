### Constructing vocab files
```
python3 vocab_main.py --train-src <src file> --train-tar <tar file> --size 50000 --freq-cutoff 2 --vocab-file vocab.bin
```
python3 vocab_main.py --train-src data/train.en-az.az.txt --size 50000 --freq-cutoff 2 --vocab-src vocab/en-az.az.bin