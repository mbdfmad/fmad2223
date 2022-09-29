#S07-005
DF0_fit_influence = DF0_fit.get_influence()
DF0_hatValues = DF0_fit_influence.hat_matrix_diag
any(DF0_hatValues > 4 / n)