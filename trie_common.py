#!/usr/bin/python
# -*- coding: utf-8 -*-

import marisa_trie


def build_trie(word_list):
    return marisa_trie.Trie([(unicode(s, "utf-8") if not isinstance(s, unicode) else s) for s in word_list])

def build_trie_from_files():
    dictionary_files = [
        'output/ahospital_anatomy_sites.txt',
        'output/ahospital_chart.txt',
        'output/ahospital_letters.txt',
        'output/ahospital_medicine.txt',
        'output/ahospital_TEST.txt',
        'output/ahospital_WHO.txt',
        'output/drug_39.txt',
        'output/jbk.txt',
        'output/jbk_drug.txt',
        'output/jbk_labtest.txt',
        'output/jbk_procedure.txt',
        'output/jbk_disease.txt',
        'output/jk_jibing.txt',
        'output/mail_cnki.txt',
        'output/medbaike_diseases.txt',
        'output/medbaike_symptom.txt',
        'output/medbaike_physical_test.txt',
        'output/medbaike_chemical_test.txt'
    ]
    list = []
    for file in dictionary_files:
        with open(file, 'r') as f:
            for line in f:
                list.append(line.replace('\n', ''))

    trie = marisa_trie.Trie([unicode(s, "utf-8") for s in list])
    trie_reverse = marisa_trie.Trie([unicode(s, "utf_8")[::-1] for s in list])
    return trie, trie_reverse

def build_trie_en():
    dict_file = 'english_notes_dataset/dict_en.txt'
    list = []
    with open(dict_file, 'r') as f:
        for line in f:
            parts = line.split(' (')
            name = ''.join(parts[:-1])
            list.append(name)
    trie = marisa_trie.Trie([unicode(s, "utf-8") for s in list])
    trie_reverse = marisa_trie.Trie([unicode(' '.join(name.split(' ')[::-1]), 'utf-8') for name in list])
    return trie, trie_reverse

