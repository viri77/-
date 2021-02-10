import itertools


def is_stressful(subj):
    k = ''.join(c for c, _ in itertools.groupby(''.join(subj.split('.')).lower()))
    b = ''.join(c for c, _ in itertools.groupby(''.join(subj.split('!')).lower()))
    c = ''.join(c for c, _ in itertools.groupby(''.join(subj.split('-')).lower()))

    if subj.isupper() or subj.endswith(
            "!!!") or 'help' in k or 'help' in b or 'help' in c or 'asap' in k or 'asap' in b or 'asap' in c or 'urgent' in k or 'urgent' in b or 'urgent' in c:

        return True
    else:
        return False



