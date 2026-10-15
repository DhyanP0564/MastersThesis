# Run makeglossaries for the acronym list (glossaries package, `acronym` option).
add_cus_dep('acn', 'acr', 0, 'makeglossaries');
sub makeglossaries {
    my ($base_name, $path) = fileparse($_[0]);
    return system("makeglossaries -d '$path' '$base_name'");
}
push @generated_exts, 'acn', 'acr', 'alg', 'ist';
