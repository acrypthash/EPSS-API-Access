# EPSS-API-Access

Weekly import of EPSS vulnerabilities


Vulnerability remediation has some fundamental truths. First, there are too many vulnerabilities to fix them all immediately. Past research has shown that firms are able to fix between 5% and 20% of known vulnerabilities per month. Secondly, only a small subset (2%-7%) of published vulnerabilities
are ever seen to be exploited in the wild. These truths set up both the need and the justification for good prioritization techniques since firms both cannot and do not need to fix everything immediately.

Vulnerability remediation
Therefore, what is the optimal prioritization strategy when remediating vulnerabilities? Unfortunately, there is no one single answer to that question, but instead lies with a collection of metrics to help inform and guide the prioritization decisions, which is where this research comes in.

The Exploit Prediction Scoring System (EPSS) is a community-driven effort to combine descriptive information about vulnerabilities (CVEs) with evidence of actual exploitation in-the-wild. By collecting and analyzing these data, EPSS seeks to improve vulnerability prioritization by estimating
the likelihood that a vulnerability will be exploited. The EPSS model produces a probability score between 0 and 1 (0% and 100%). The higher the score, the greater the probability that a vulnerability will be exploited (in the next 30 days).
