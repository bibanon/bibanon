use warnings;
use strict;
use Parallel::ForkManager;
use 5.010;
my $pm=new Parallel::ForkManager(50);

use Fcntl qw(:flock SEEK_END);

$pm->run_on_finish(sub{
    my (undef, undef, undef, undef, undef, $res_ref) = @_;
    my ($res, $line) = @$res_ref;
    if ($res == 1) {
            open my $outf, ">>", "outf";
            flock($outf, LOCK_EX) or next;
            seek($outf, 0, SEEK_END);
            say $outf $line;
            say $line;
            flock($outf, LOCK_UN);
    }
});

my $i = 1;
while (1) {
    $i++;
    $pm->start and next;
    my $res;
    my $page="";

    $page = `curl -s http://thepiratebay.se/torrent/$i -m 120` 
        while ($page !~ /<!DOCTYPE html/);
    my $line = "";
    if ($page =~ m{<title>Not Found}) {
        $res = 0;
    } else {
        $res = 1;
        my ($title) = $page =~ /<div id="title">\s*(.*?)\s*<\/div>/s;
        my ($size) = $page =~ /<dt>Size:<\/dt>\s*<dd>.*?\((\d*)&nbsp;Bytes\)<\/dd>/s;
        my ($seeders) = $page =~ /<dt>Seeders:<\/dt>\s*<dd>(\d*)<\/dd>/;
        my ($leechers) = $page =~ /<dt>Leechers:<\/dt>\s*<dd>(\d*)<\/dd>/;
        my ($magnet) = $page =~ /magnet:\?xt=urn:btih:(.*?)(&|")/;
        $line =
        $i."|".$title."|".$size."|".$seeders."|".$leechers."|".$magnet;
    }
    $pm->finish(0,[$res, $line]);
}