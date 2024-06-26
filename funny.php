<?php
$ip = $_SERVER['REMOTE_ADDR'];
$escaped_ip = escapeshellarg($ip);
$output_file = tempnam(sys_get_temp_dir(), 'ipgif_') . '.gif';
shell_exec("python3 generate_gif.py $escaped_ip $output_file");
header('Content-Type: image/gif');
readfile($output_file);
unlink($output_file);
