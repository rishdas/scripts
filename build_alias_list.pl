#!/usr/bin/perl

use strict;

my @a_out;
my @a_str;
my $str;
my $file;

open INFILE, "<host_list"
    or die "can't open file: $!";

open OUTFILE, ">file_parse.out"
    or die "can't open file: $!";

while(<INFILE>)
{
    chomp($_);
    @a_str = split(/\./, $_);

    print (OUTFILE "alias $a_str[0]=\'ssh sirdas\@$_\'");
    print (OUTFILE "\n");
}

close INFILE
    or die "can't close file: $!";

close OUTFILE
    or die "can't close file: $!";
