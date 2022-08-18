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

# Brew Day Checklist  
<label name="var_label" for="bdate">Brew Date</label><input type="date" id="bdate" name="bdate" required>
<label name="var_label" for="style">Beer Style</label><input type="text" id="style" name="style" required>

## ⚠️ info  
* 

## 📋 prep  
- [X] Sanitize ferment and serving keg.
- [X] Filter Strike Volume into boil kettle, then heat to 100°F.
- [X] Add 1.0 g/gal each of bread yeast and sugar.
- [X] Weigh grains into bucket.
- [X] Measure Irish moss and rehydrate in water. Measure minerals, hops, adjuncts.
- [X] Set up brewing equipment (kettle, MLT, chiller, cart, grain mill, close valves).
- [X] Adjust grain mill gap spacing (0.028 in).

## 📋 set-up  
- [ ] Begin heating strike water in Boil Kettle at 75% heat.
- [ ] Dose bottom of mash bag with minerals.
- [ ] Condition pre-measured grains, and rest for 10 minutes.
- [ ] Connect CO₂ to Boil Kettle hose, and purge plumbing and MLT at 1 psi CO₂.
- [ ] Mill grains into MLT.
- [ ] Dose HLT with SMB.

## 📋 mash  
- [ ] Set Boil Kettle to MLT pump flow, open Kettle valve to flood pump line with strike water.
- [ ] Open MLT valve, and pump strike water volume to MLT (0.6 GPM = 6% power).
- [ ] Turn off pump, close MLT valve, then close Boil Kettle valve.
- [ ] Add acid/sauergut to MLT, stir mash gently to mix thoroughly, and cover with mash cap.
- [ ] Set RIMS recirculation pump flow, open MLT valve.
- [ ] Rest mash for 5 minutes, then turn on pump and recirculate for 5 minutes (0.6 GPM).
- [ ] Slowly increase recirculation to 2.0 GPM while turning on element PID, and set first mash step.
- [ ] Mash per schedule, and record data in log.
- [ ] After first β rest, and measure/adjust mash pH.
- [ ] At end of mash, turn off PID, turn off pump, and close MLT valve.

## 📋 mash out  
- [ ] Set MLT to Boil Kettle pump flow, open MLT valve, and  flood pump line with wort.
- [ ] Open Boil Kettle valve and pump wort volume to Kettle at #2 on controller (0.5 GPM).
- [ ] When wort level in MLT reaches grain bed, pump sparge water to top of MLT through sample valve and RIMS.
- [ ] When Boil Kettle reaches pre-boil volume, close Boil Kettle valve, and turn off all pumps.
- [ ] Stir Kettle wort thoroughly, measure pre-boil volume/°B. Adjust with Gravity Dilution Calculator as needed.
- [ ] Drain remaining second runnings through sample valve for yeast propagation, sauergut, and barley tea.

## 📋 boil  
- [ ] Attach 2 binder clips 90° apart on Boil Kettle, and set to boil mark on burner to bring wort to a gentle boil.
- [ ] *OPTIONAL: Create vitality starter for yeast using second runnings.*
- [ ] Add Fermcap (9 drops), and skim any accumulated foam as it approaches a boil.
- [ ] Make hot scotchy and begin cleaning MLT and plumbing.
- [ ] Add hops (0:30).
- [ ] At 15 minutes before end of boil, flame out, measure wort volume, °B, and pH.
- [ ] Replace lid and adjust boil length as necessary, then re-ignite flame.
- [ ] Add acid boil additions, Irish Moss (0:15), ellagic acid (0:06).
- [ ] Begin sanitizing post-boil equipment, including wort chiller.
- [ ] Flame out, measure wort volume.

## 📋 chill & pitch  
- [ ] Submerge sanitized wort chiller, mount stirrer, and turn Boil Kettle pick-up tube to 10:00 orientation.
- [ ] Activate wort chiller and stirrer, then cool to 170°F.
- [ ] Add whirlpool hop addition in mesh bag.
- [ ] Re-activate wort chiller and stirrer, then cool to less than 70°F (recover hot waste water for cleaning).
- [ ] Remove wort chiller, then whirlpool with stirrer for 2 minutes.
- [ ] Raise valve edge of Boil Kettle on block, and wait 30 minutes to settle trub.
- [ ] Prep fermenter and serving keg, then continue equipment clean-up.
- [ ] Turn pick-up tube to 12:00 orientation, and transfer wort to fermentation vessel.
- [ ] Transfer trub, record trub volume, and transfer to pitcher in fridge to reserve as speise for spunding and FFT.
- [ ] Cap fermentation vessel, seat lid with CO₂ to 10 psi, and move to fermentation chamber.
- [ ] Relax, don't worry, have a homebrew.
- [ ] *Begin fermentation schedule.*

## ✏️ notes  
<textarea id="notes" name="notes" rows="12" required></textarea>
