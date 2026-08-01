# Brew Day Checklist

<style>
	input[name=style], input[name=bdate] {
	padding: 2px 10px 5px 5px;
	margin: 0 0 15px 0;
	display: block;
	width: 220px;
	font-size: 14px;
	text-align: left;
	border: none;
	border-radius: 0;
	border-bottom: 1px solid #c6c6c6;
	outline: none;
	transition: 0.2s;
	}

	textarea {
	padding: 2px 10px 5px 5px;
	margin: 0 0 15px 0;
	display: block;
	width: 80%;
	font-size: 14px;
	border-radius: 0;
	border: 1px solid #c6c6c6;
	outline: none;
	transition: 0.2s;
	resize: none;
	}

	input[name=style]:focus, input[name=bdate]:focus {
	border-bottom: 2px solid #2196f3;
	}

	textarea:focus {
	border: 2px solid #2196f3;
	}

	label[name=var_label] {
	font-size: 16px;
	}
</style>

<label name="var_label" for="bdate">Brew Date</label><input type="date" id="bdate" name="bdate" required>
<label name="var_label" for="style">Beer Style</label><input type="text" id="style" name="style" required>

## ⚠️ info
* 

## 📋 set-up
- [ ] Filter Strike Volume into HLT (and Sparge Volume into bucket if necessary).
- [ ] Heat Strike Volume to 100°F.
- [ ] Measure Irish moss and rehydrate in water.
- [ ] Add 1.0 g/gal each of bread yeast and sugar, and rest for 90 minutes.
- [ ] Prep brewing equipment (kettle, MLT, mash bag, chiller, cart, grain mill, close valves).
- [ ] Measure MLT minerals and dose into MLT (CaSO₄, CaCl₂, NaCl, Ellagic).
- [ ] Measure HLT minerals (NaMeta).
- [ ] Measure End of Boil minerals (Ellagic, Yeast Nutrient)
- [ ] Measure hops and adjuncts.
- [ ] Adjust grain mill gap spacing (0.028 in).
- [ ] Weigh grains into bucket.

## 📋 mash
- [ ] Begin heating strike water to Strike Temperature.
- [ ] Condition pre-measured grains, and rest for 10 minutes.
- [ ] Mill grains into MLT.
- [ ] Dose HLT with NaMeta.
- [ ] Set HLT to MLT underlet pump flow, open HLT valve to flood pump line with strike water.
- [ ] Open MLT valve, and pump strike water volume to MLT (0.6 GPM = 6-8% power).
- [ ] Close MLT valve, turn off pump, then close Boil Kettle valve.
- [ ] Add mash acid to MLT, stir mash gently to mix thoroughly, and cover with mash cap.
- [ ] Set RIMS recirculation pump flow, open MLT valve.
- [ ] Rest mash for 5 minutes, then turn on pump and recirculate for 5 minutes (0.6 GPM).
- [ ] Slowly increase recirculation to 2.0 GPM while turning on element PID, and set first mash step.
- [ ] Mash per schedule, and record data for each rest in log.
- [ ] After second β rest, and measure/adjust mash pH.
- [ ] To end mash, turn off PID, turn off pump, and close MLT valve.

## 📋 mash out
- [ ] Set HLT to MLT sparge pump flow, open Kettle valve to flood pump line with sparge water.
- [ ] Open RIMS valve, and pump sparge water volume to MLT (0.6 GPM = 6% power).
- [ ] Set MLT to Boil Kettle pump flow, open MLT valve, and flood pump line with wort.
- [ ] Open Boil Kettle valve and pump wort volume to Kettle (0.6 GPM).
- [ ] When Boil Kettle reaches pre-boil volume, close Boil Kettle valve, and turn off all pumps.
- [ ] Stir Kettle wort thoroughly, measure pre-boil volume/°B. Adjust with Gravity Dilution Calculator as needed.
- [ ] Drain remaining second runnings through sample valve for yeast propagation, sauergut, and barley tea.

## 📋 boil
- [ ] Add Fermcap (9 drops), and bring Boil Kettle to a rolling simmer with no lid.
- [ ] Begin cleaning MLT and plumbing.
- [ ] Add hops.
- [ ] Add acid/Irish Moss (0:15) and ellagic acid/nutrient (0:06).
- [ ] Begin sanitizing post-boil equipment, including wort chiller.
- [ ] Flame out, measure wort volume, °B, and pH.

## 📋 chill
- [ ] Submerge sanitized wort chiller, mount stirrer, and turn Boil Kettle pick-up tube to 09:00 orientation.
- [ ] Activate wort chiller and stirrer, then cool to 180°F.
- [ ] Add whirlpool hop addition in mesh bag.
- [ ] Re-activate wort chiller and stirrer, then cool to less than 70°F (recover hot waste water for cleaning).
- [ ] Remove wort chiller, then whirlpool with stirrer for 2 minutes.
- [ ] Raise valve edge of Boil Kettle on block, and wait 30 minutes to settle trub.
- [ ] Prep and sanitize fermenter and serving keg, then continue equipment clean-up.
- [ ] Transfer wort to fermentation vessel.
- [ ] Transfer trub to pitcher, record trub volume, and chill in fridge reserving as speise for spunding/FFT.

## 📋 pitch
- [ ] Strap temperature probe to fermenter, and chill wort in FV to fermentation temp if necessary.
- [ ] Aerate wort with O₂ (4 mins at 0.25 L/min), wait 5 minutes, repeat aeration, wait 5 minutes again.
- [ ] Add FAA, then pitch yeast.
- [ ] Link fermenter In post to serving keg Out post, and connect CO₂ to serving keg In post.
- [ ] Pressurize and correct any leaks.
- [ ] Remove CO₂, and connect blow-off to serving keg In post.

## ✏️ notes
<textarea id="notes" name="notes" rows="12" required></textarea>
