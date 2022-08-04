=====
Usage
=====

To use zeeklog2pandas in a project::

    from zeeklog2pandas.zeeklog2pandas import read_zeek

    df = read_zeek('ssl.log')

    print(df)

    ts                 uid    id.orig_h  id.orig_p    id.resp_h  ...  validation_status notary.first_seen notary.last_seen notary.times_seen notary.valid
    0 2021-12-31 22:59:55.174243072   CDy3UFvdbDmFSrPW9  192.168.1.1      40344  192.168.1.2  ...                  -                 -                -                 -            -
    1 2021-12-31 22:59:55.326785024  CUobJa1lv9mEKpaAY1  192.168.1.2      37676  192.168.2.1  ...                  -                 -                -                 -            -

    [2 rows x 25 columns]
