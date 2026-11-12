# region ---- TB of data in S3 (images, unless otherwise noted)
images_tb = [
    19,  # spitzer
    31,  # allsky
    10,  # 3band
    12,  # postcryo
    13,  # allwise
    350 - (4 * 9),  # neowiser (total - catalogs)  # [CHECKME] I think final is 400T.
    8.5,  # open universe
    # 5,  # unwise (catalog)
    40,  # euclid (imaging and spectroscopy)
]

sum(images_tb)

# endregion - TB of data in S3 (images)

# region ---- Number of rows in S3 (catalogs)

import pyarrow.dataset

linkbase = "/stage/irsa-data-parquetlinks/links-ops"
catalogs = [
    # allwise
    f"{linkbase}/wise/allwise/healpix_k5/wise-allwise.parquet",
    # neowise
    *[
        f"{linkbase}/neowiser/healpix_k5/year{N}/neowiser-healpix_k5-year{N}.parquet"
        for N in range(1, 10)
    ],
    # unwise
    f"{linkbase}/unwise/neo7/time_domain/healpix_k5/unwise-neo7-time_domain-healpix_k5.parquet/",
]

numrows = []
for catalog in catalogs:
    meta = pyarrow.dataset.parquet_dataset(f"{catalog}/_metadata")
    nrows = sum(frag.metadata.num_rows for frag in meta.get_fragments())
    numrows.append(nrows)
    print(catalog, nrows)

# /stage/irsa-data-parquetlinks/links-ops/wise/allwise/healpix_k5/wise-allwise.parquet 747634026
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year1/neowiser-healpix_k5-year1.parquet 18468575586
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year2/neowiser-healpix_k5-year2.parquet 19691230571
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year3/neowiser-healpix_k5-year3.parquet 19631135692
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year4/neowiser-healpix_k5-year4.parquet 19098199664
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year5/neowiser-healpix_k5-year5.parquet 18795708783
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year6/neowiser-healpix_k5-year6.parquet 18717323537
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year7/neowiser-healpix_k5-year7.parquet 18784693939
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year8/neowiser-healpix_k5-year8.parquet 18668416994
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year9/neowiser-healpix_k5-year9.parquet 18650186132
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year9/neowiser-healpix_k5-year10.parquet 18371369954
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year9/neowiser-healpix_k5-year11.parquet 10848820857
# /stage/irsa-data-parquetlinks/links-ops/neowiser/healpix_k5/year9/neowiser-healpix_k5-addendum.parquet 36759434

sum(numrows)
# 200510055169

# endregion - Number of rows in S3 (catalogs)
