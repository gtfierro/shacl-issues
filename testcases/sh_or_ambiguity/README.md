# `sh:or` Ambiguity

The test case contains a NodeShape with an `or` clause containing 2 branches,
and 2 instances which are validated against that NodeShape. The generated
report (correctly) says the model validates, but it does not indicate *why*
the 2 instances passed validation. Specifically, the report does not say which
`or` case was satisfied by each instance.
