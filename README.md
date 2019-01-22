<h1>MCVanillaServerFinder</h1>
This tool lets you easily scan for 100% vanilla Minecraft Servers starting from one or more IPs of your choice. Usage is listed below.
<h2>Usage</h2>
<p>usage: serverfinder.py [-h] [--pnum PNUM] [--depth DEPTH] [--minp MINP[--maxp MAXP]
                       startip mcversion</p>

<p>positional arguments:</p>
<li><strong>startip</strong>        The IP(s) to begin the search from. Interval with a comma and
                 no spaces.
  <li><strong>mcversion</strong>      The version(s) to search for. Interval with a comma and no
                 spaces.
<br />

<p>optional arguments:</p>
<li><strong>--pnum PNUM</strong>    Number of processes</li>
  <li><strong>--depth DEPTH</strong>  Depth of IP scan (between 1 and 2)</li>
  <li><strong>--minp MINP</strong>    Minimum amount of players atm</li>
  <li><strong>--maxp MAXP</strong>    Maximum amount of players atm</li>
      <br />
      The script will output to a file named 'results.txt'
  <h2>Warnings</H2>
  <li>Note that a level 2 scan corresponds to a full /16 subnet mask so expect much longer wait times.</li>
  <li>I am by no means an expert Python programmer, so the code is definitely untidy and not optimized, it's just a script that I 've quickly put together because I thought it would be useful. I'm also just getting started with GitHub so bear with me for any mistakes.</li>
  <h2>Requirements</h2>
  <li><strong>mcstatus</strong> by Dinnerbone (https://github.com/Dinnerbone/mcstatus)
  <li><strong>argparse</strong>
