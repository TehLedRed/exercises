test_that("Ex 1 Atbash cipher", {
    
    expect_equal(encrypt("test"), "gvhg")

    expect_equal(encrypt("x123 yes"), "c123b" "vh")

    expect_equal(encrypt("gvhg"), "test")

    expect_equal(
        encrypt("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt", 0),
        "thequickbrownfoxjumpsoverthelazydog"
    )

})
