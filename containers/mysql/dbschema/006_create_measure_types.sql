--
-- MyMONIT DB Schema definition
-- 
--
-- definition of the MEASURE_TYPES table

use my_monit;

-- models the type of a measure as
-- * id: synthetic key
-- * name: type's name

CREATE TABLE MEASURE_TYPES
(
    ID                  SMALLINT       NOT NULL AUTO_INCREMENT,
    NAME                VARCHAR(14)    NOT NULL,
    SYMBOL              VARCHAR(3)     NOT NULL,
    QUANTITY            VARCHAR(61)    NOT NULL,

    PRIMARY KEY(ID)
);

INSERT INTO MEASURE_TYPES(NAME, SYMBOL, QUANTITY) VALUES
    ('hertz',           'Hz',   'frequency'),
    ('radian',          'rad',  'angle'),
    ('steradian',       'sr',   'solid angle'),
    ('newton',          'N',    'force, weight'),
    ('pascal',          'Pa',   'pressure, stress'),
    ('joule',           'J',    'energy, work, heat'),
    ('watt',            'W', 	'power, radiant flux'),
    ('coulomb',         'C',    'electric charge or quantity of electricity'),
    ('volt',    	    'V',    'voltage, electrical potential difference, electromotive force'),
    ('farad',  	        'F', 	'electrical capacitance'),
    ('ohm',  	        'Ω', 	'electrical resistance, impedance, reactance'),
    ('siemens', 	    'S', 	'electrical conductance'),
    ('weber', 	        'Wb', 	'magnetic flux'),
    ('tesla',           'T', 	'magnetic induction, magnetic flux density'),
    ('henry', 	        'H', 	'electrical inductance'),
    ('degree Celsius',  '°C',   'temperature relative to 273.15 K'),
    ('lumen', 	        'lm', 	'luminous flux'),
    ('lux', 	        'lx', 	'illuminance'),
    ('becquerel',    	'Bq', 	'radioactivity (decays per unit time)'),
    ('gray', 	        'Gy', 	'absorbed dose (of ionizing radiation)'),
    ('sievert', 	    'Sv', 	'equivalent dose (of ionizing radiation)'),
    ('katal', 	        'kat', 	'catalytic activity');