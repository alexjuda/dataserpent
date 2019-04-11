import src.parser as dp
import src.clj as clj


def test_pattern_eav():
    assert dp.parse_clause(clj.str2edn('[?e ?a ?v]')) \
        == dp.Pattern(dp.DefaultSrc(None),
                      [dp.Variable(clj.S('?e')),
                       dp.Variable(clj.S('?a')),
                       dp.Variable(clj.S('?v'))])


def test_pattern_a():
    assert dp.parse_clause(clj.str2edn('[_ ?a _ _]')) \
        == dp.Pattern(dp.DefaultSrc(None),
                      [dp.Placeholder(None),
                       dp.Variable(clj.S('?a')),
                       dp.Placeholder(None),
                       dp.Placeholder(None)])


def test_pattern_x_a():
    assert dp.parse_clause(clj.str2edn('[$x _ ?a _ _]')) \
        == dp.Pattern(dp.SrcVar(clj.S('$x')),
                      [dp.Placeholder(None),
                       dp.Variable(clj.S('?a')),
                       dp.Placeholder(None),
                       dp.Placeholder(None)])


def test_pattern_x_name_v():
    assert dp.parse_clause(clj.str2edn('[$x _ :name ?v]')) \
        == dp.Pattern(dp.SrcVar(clj.S('$x')),
                      [dp.Placeholder(None),
                       dp.Constant(clj.K('name')),
                       dp.Variable(clj.S('?v'))])


def test_pred_a_1():
    clause = clj.str2edn('[(pred ?a 1)]')
    expected = dp.Predicate(dp.PlainSymbol(clj.S('pred')),
                            [dp.Variable(clj.S('?a')), dp.Constant(1)])
    assert dp.parse_clause(clause) == expected


def test_pred():
    clause = clj.str2edn('[(pred)]')
    expected = dp.Predicate(dp.PlainSymbol(clj.S('pred')), [])
    assert dp.parse_clause(clause) == expected


def test_pred_custom():
    clause = clj.str2edn('[(?custom-pred ?a)]')
    expected = dp.Predicate(dp.PlainSymbol(clj.S('?custom-pred')),
                            [dp.Variable(clj.S('?a'))])
    assert dp.parse_clause(clause) == expected
