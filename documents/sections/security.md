# Security

Using the STRIDE model, the following threats were identified and classified with DREAD.

## Spoofing

### User's credentials violation

| Type | Level |
|------|-------|
| Damage | High, experiments would be exposed, users' records compromised, data leak |
| Reproducibility | High |
| Exploitability | High |
| Affected users | One user. All, if the user is administrator |
| Discoverability | Medium. User's credentials may be easy to guess |

## Tampering

### Introducing fake measurements on the message broker

| Type | Level |
|------|-------|
| Damage | High, experiments would be invalidated |
| Reproducibility | Medium. The highest risk is broker's authentication |
| Exploitability | High. Discovering credentials would make it easy to exploit the vulnerability |
| Affected users | All scientists |
| Discoverability | Medium. The broker is public, but credentials are highly secure |

## Repudiation

Scientists will not be able to manipulate the association between them and the experiments, or between the experiments and the data. Data will not be editable.

## Information disclosure

### Database breach

| Type | Level |
|------|-------|
| Damage | High, data would be exposed |
| Reproducibility | Low. Database is not directly exposed, authentication is in place |
| Exploitability | Low. Attacker should compromise at least another system first |
| Affected users | All |
| Discoverability | Low |


## Denial of service

### DDos on APIs

| Type | Level |
|------|-------|
| Damage | High, system may become inoperative |
| Reproducibility | Low. The system should be exposed only in the internal network |
| Exploitability | Low. It would be easy to block the attack in the internal network |
| Affected users | All |
| Discoverability | Low. It would be difficult to plan an effective attack. |

## Elevation of privilege

### Scientists becoming administrators

| Type | Level |
|------|-------|
| Damage | High, the attacker could disrupt the system |
| Reproducibility | Low. It would require database access since no system function manipulates roles |
| Exploitability | Low. Attacker should compromise at least another system first |
| Affected users | All |
| Discoverability | Low |
