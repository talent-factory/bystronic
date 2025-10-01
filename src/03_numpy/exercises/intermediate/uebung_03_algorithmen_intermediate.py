#!/usr/bin/env python3
"""
NumPy Übung 3: Numerische Algorithmen und Signalverarbeitung (Intermediate)
SmartFactory Python Grundkurs - Kapitel 3

Diese Übung behandelt erweiterte numerische Algorithmen und Signalverarbeitung
mit NumPy für technische Anwendungen in der Produktion.

Lernziele:
- Numerische Integration und Differentiation
- Signalverarbeitung und Filterung
- Fourier-Transformationen für Frequenzanalyse
- Interpolation und Kurvenanpassung
- Optimierungsalgorithmen mit NumPy
- Praktische Anwendungen für SmartFactory-Szenarien

Schwierigkeitsgrad: 🟡 Intermediate
Geschätzte Bearbeitungszeit: 45-50 Minuten
"""

import time
import warnings

import numpy as np

warnings.filterwarnings("ignore")


def main():
    """Hauptfunktion für alle numerische Algorithmus-Übungen"""
    print("🎯 NUMPY INTERMEDIATE ÜBUNG 3: NUMERISCHE ALGORITHMEN & SIGNALVERARBEITUNG")
    print("=" * 80)
    print("Diese Übung behandelt erweiterte numerische Methoden und")
    print("Signalverarbeitung für technische SmartFactory-Anwendungen.")
    print()

    try:
        # Aufgabe 1: Numerische Integration und Differentiation
        aufgabe_1_numerical_calculus()

        # Aufgabe 2: Signalverarbeitung und Filterung
        aufgabe_2_signal_processing()

        # Aufgabe 3: Fourier-Analyse für Frequenzdomäne
        aufgabe_3_fourier_analysis()

        # Aufgabe 4: Interpolation und Kurvenanpassung
        aufgabe_4_interpolation_fitting()

        # Aufgabe 5: Optimierung und Root-Finding
        aufgabe_5_optimization()

        print("\n" + "🎉" * 70)
        print("🎉 ALLE NUMERISCHE ALGORITHMUS-AUFGABEN ABGESCHLOSSEN! 🎉")
        print("🎉" * 70)
        print("\n📋 GELERNTE KONZEPTE:")
        print("✅ Numerische Integration (Trapez, Simpson)")
        print("✅ Finite Differenzen für Ableitungen")
        print("✅ Signalfilterung und Rauschunterdrückung")
        print("✅ FFT für Frequenzanalyse")
        print("✅ Interpolation und Spline-Fitting")
        print("✅ Numerische Optimierung")

    except KeyboardInterrupt:
        print("\n\n⚠️ Übung abgebrochen.")
    except Exception as e:
        print(f"\n❌ Fehler in der Übung: {e}")
        print("💡 Tipp: Prüfen Sie Eingabeparameter und Array-Dimensionen!")


def aufgabe_1_numerical_calculus():
    """Aufgabe 1: Numerische Integration und Differentiation"""
    print("🎯 AUFGABE 1: NUMERISCHE INTEGRATION UND DIFFERENTIATION")
    print("-" * 60)
    print("Ziel: Implementiere numerische Methoden für Calculus-Operationen")
    print("mit Anwendung auf Produktionsdaten und Maschinensignale")
    print()

    start_time = time.time()

    # 1.1 Numerische Integration
    print("📊 1.1 Numerische Integration:")

    def trapezoidal_rule(y_values, x_values=None, dx=1.0):
        """Trapezregel für numerische Integration"""
        if x_values is not None:
            # Ungleichmäßige Abstände
            dx_array = np.diff(x_values)
            integral = np.sum((y_values[:-1] + y_values[1:]) * dx_array / 2)
        else:
            # Gleichmäßige Abstände
            integral = np.sum((y_values[:-1] + y_values[1:]) * dx / 2)
        return integral

    def simpson_rule(y_values, dx=1.0):
        """Simpson-Regel für numerische Integration (gerade Anzahl Intervalle)"""
        n = len(y_values)
        if n % 2 == 0:
            n -= 1  # Mache ungerade für Simpson-Regel
            y_values = y_values[:n]

        # Simpson 1/3 Regel
        integral = y_values[0] + y_values[-1]
        integral += 4 * np.sum(y_values[1::2])  # Ungerade Indizes
        integral += 2 * np.sum(y_values[2:-1:2])  # Gerade Indizes (außer Enden)
        integral *= dx / 3

        return integral

    # Test mit Maschinendaten: Leistungsaufnahme über Zeit
    print("  Anwendung: Integration der Leistungsaufnahme (Energieverbrauch)")

    # Simuliere Leistungskurve einer CNC-Maschine über 8-Stunden Schicht
    t_hours = np.linspace(0, 8, 481)  # Alle Minuten
    dt = t_hours[1] - t_hours[0]

    # Realistische Leistungskurve
    power_base = 30  # kW Grundverbrauch
    power_cycle = 15 * np.sin(2 * np.pi * t_hours / 2)  # 2h Zyklen
    power_noise = 2 * np.random.randn(len(t_hours))
    power_kw = power_base + power_cycle + power_noise
    power_kw = np.maximum(power_kw, 5)  # Minimum 5kW

    print(f"    Zeitbereich: {t_hours[0]:.1f} - {t_hours[-1]:.1f} Stunden")
    print(f"    Leistungsbereich: {np.min(power_kw):.1f} - {np.max(power_kw):.1f} kW")

    # Verschiedene Integrationsmethoden
    energy_trapez = trapezoidal_rule(power_kw, t_hours)
    energy_simpson = simpson_rule(power_kw, dt)
    energy_numpy = np.trapz(power_kw, t_hours)  # NumPy's eingebaute Funktion

    print("\n    Energieverbrauch-Berechnung:")
    print(f"      Trapezregel:     {energy_trapez:.2f} kWh")
    print(f"      Simpson-Regel:   {energy_simpson:.2f} kWh")
    print(f"      NumPy trapz:     {energy_numpy:.2f} kWh")

    # Vergleich mit analytischer Lösung (nur für den glatten Teil)
    analytical_base = power_base * 8
    analytical_cycle = 0  # Integral von sin über ganzen Zyklus ist 0
    analytical_total = analytical_base  # Ohne Rauschen

    print(f"      Analytisch (ohne Rauschen): {analytical_total:.2f} kWh")

    # 1.2 Numerische Differentiation
    print("\n📊 1.2 Numerische Differentiation:")

    def finite_difference_1st(y, dx=1.0, method="central"):
        """Erste Ableitung mit finiten Differenzen"""
        if method == "forward":
            # Vorwärtsdifferenz: f'(x) ≈ (f(x+h) - f(x))/h
            dy = np.diff(y) / dx
            # Extrapoliere letzten Punkt
            dy = np.append(dy, dy[-1])

        elif method == "backward":
            # Rückwärtsdifferenz: f'(x) ≈ (f(x) - f(x-h))/h
            dy = np.diff(y) / dx
            # Extrapoliere ersten Punkt
            dy = np.insert(dy, 0, dy[0])

        elif method == "central":
            # Zentrale Differenz: f'(x) ≈ (f(x+h) - f(x-h))/(2h)
            dy = np.zeros_like(y)
            dy[1:-1] = (y[2:] - y[:-2]) / (2 * dx)
            # Randbehandlung
            dy[0] = (y[1] - y[0]) / dx  # Vorwärts am Anfang
            dy[-1] = (y[-1] - y[-2]) / dx  # Rückwärts am Ende

        return dy

    def finite_difference_2nd(y, dx=1.0):
        """Zweite Ableitung mit finiten Differenzen"""
        # f''(x) ≈ (f(x+h) - 2f(x) + f(x-h))/h²
        d2y = np.zeros_like(y)
        d2y[1:-1] = (y[2:] - 2 * y[1:-1] + y[:-2]) / (dx**2)

        # Randbehandlung mit Extrapolation
        d2y[0] = d2y[1]
        d2y[-1] = d2y[-2]

        return d2y

    # Anwendung: Vibrationsanalyse
    print("  Anwendung: Vibrationsanalyse einer Spindel")

    # Simuliere Vibrationsignal
    fs = 1000  # Sampling-Frequenz in Hz
    t_vib = np.linspace(0, 2, 2 * fs)  # 2 Sekunden
    dt_vib = t_vib[1] - t_vib[0]

    # Zusammengesetztes Signal: Grundfrequenz + Harmonische + Rauschen
    freq_fundamental = 50  # Hz (Hauptspindel)
    freq_harmonic = 150  # Hz (3. Harmonische)

    displacement = (
        0.1 * np.sin(2 * np.pi * freq_fundamental * t_vib)
        + 0.03 * np.sin(2 * np.pi * freq_harmonic * t_vib)
        + 0.01 * np.random.randn(len(t_vib))
    )

    # Berechne Geschwindigkeit und Beschleunigung
    velocity = finite_difference_1st(displacement, dt_vib, "central")
    acceleration = finite_difference_2nd(displacement, dt_vib)

    # Analytische Vergleichswerte für Validierung
    velocity_analytical = 0.1 * 2 * np.pi * freq_fundamental * np.cos(
        2 * np.pi * freq_fundamental * t_vib
    ) + 0.03 * 2 * np.pi * freq_harmonic * np.cos(2 * np.pi * freq_harmonic * t_vib)

    acceleration_analytical = -0.1 * (2 * np.pi * freq_fundamental) ** 2 * np.sin(
        2 * np.pi * freq_fundamental * t_vib
    ) - 0.03 * (2 * np.pi * freq_harmonic) ** 2 * np.sin(
        2 * np.pi * freq_harmonic * t_vib
    )

    print(f"    Signal: {len(t_vib):,} Samples @ {fs} Hz")
    print(f"    Frequenzen: {freq_fundamental} Hz + {freq_harmonic} Hz")

    # RMS-Fehler zwischen numerisch und analytisch
    rms_velocity_error = np.sqrt(np.mean((velocity - velocity_analytical) ** 2))
    rms_acceleration_error = np.sqrt(
        np.mean((acceleration - acceleration_analytical) ** 2)
    )

    print("\n    RMS-Fehler (numerisch vs. analytisch):")
    print(f"      Geschwindigkeit:   {rms_velocity_error:.6f} m/s")
    print(f"      Beschleunigung:    {rms_acceleration_error:.6f} m/s²")

    # Statistische Auswertung
    displacement_rms = np.sqrt(np.mean(displacement**2))
    velocity_rms = np.sqrt(np.mean(velocity**2))
    acceleration_rms = np.sqrt(np.mean(acceleration**2))

    print("\n    RMS-Werte der Vibrationssignale:")
    print(f"      Auslenkung:        {displacement_rms:.6f} m")
    print(f"      Geschwindigkeit:   {velocity_rms:.6f} m/s")
    print(f"      Beschleunigung:    {acceleration_rms:.6f} m/s²")

    # 1.3 Numerische Integration von gemessenen Daten
    print("\n📊 1.3 Integration von realen Messdaten:")

    # Simuliere ungleichmäßig abgetastete Drehmoment-Messung
    n_measurements = 500
    t_torque = np.sort(
        np.random.uniform(0, 10, n_measurements)
    )  # Ungleichmäßige Zeitpunkte
    torque_nm = 100 + 50 * np.sin(0.5 * t_torque) + 10 * np.random.randn(n_measurements)

    print(f"    Drehmoment-Messungen: {n_measurements} ungleichmäßige Samples")
    print(f"    Zeitbereich: {t_torque[0]:.2f} - {t_torque[-1]:.2f} s")

    # Integration für Arbeit (Work = ∫ Torque × ω dt, vereinfacht mit konstanter ω)
    omega_rpm = 1500  # U/min
    omega_rad_s = omega_rpm * 2 * np.pi / 60  # rad/s

    power_watts = torque_nm * omega_rad_s  # Leistung in Watt

    # Integration mit verschiedenen Methoden
    work_trapz = np.trapz(power_watts, t_torque)  # NumPy Trapezregel
    work_manual = trapezoidal_rule(power_watts, t_torque)  # Manuelle Implementierung

    print(f"    Rotationsgeschwindigkeit: {omega_rpm} RPM ({omega_rad_s:.1f} rad/s)")
    print("    Geleistete Arbeit:")
    print(f"      NumPy trapz:      {work_trapz:.2f} J")
    print(f"      Manuelle Trapez:  {work_manual:.2f} J")
    print(f"      Differenz:        {abs(work_trapz - work_manual):.6f} J")

    duration = time.time() - start_time
    print(f"\n⚡ Numerische Calculus in {duration:.3f} Sekunden")
    print("📐 Finite Differenzen sind essentiell für Sensordaten-Analyse!")
    print()


def aufgabe_2_signal_processing():
    """Aufgabe 2: Signalverarbeitung und Filterung"""
    print("🎯 AUFGABE 2: SIGNALVERARBEITUNG UND FILTERUNG")
    print("-" * 50)
    print("Ziel: Implementiere Signalfilterung und Rauschunterdrückung")
    print("für Maschinensensoren und Qualitätsmessungen")
    print()

    start_time = time.time()

    # 2.1 Gleitender Durchschnitt (Moving Average)
    print("📊 2.1 Gleitende Durchschnitte und Filterung:")

    def moving_average_simple(signal, window_size):
        """Einfacher gleitender Durchschnitt"""
        return np.convolve(signal, np.ones(window_size) / window_size, mode="valid")

    def moving_average_weighted(signal, window_size, weights=None):
        """Gewichteter gleitender Durchschnitt"""
        if weights is None:
            # Dreiecksfenster (mehr Gewicht in der Mitte)
            weights = np.bartlett(window_size)
        else:
            weights = np.array(weights)

        weights = weights / np.sum(weights)  # Normalisierung
        return np.convolve(signal, weights, mode="valid")

    def exponential_moving_average(signal, alpha=0.1):
        """Exponentieller gleitender Durchschnitt"""
        filtered = np.zeros_like(signal)
        filtered[0] = signal[0]

        for i in range(1, len(signal)):
            filtered[i] = alpha * signal[i] + (1 - alpha) * filtered[i - 1]

        return filtered

    # Simuliere verrauschtes Temperatursignal
    np.random.seed(42)
    t = np.linspace(0, 100, 1000)  # 100 Sekunden, 10 Hz
    temp_clean = 65 + 5 * np.sin(0.1 * t) + 2 * np.sin(0.05 * t)  # Sauberes Signal
    noise = 3 * np.random.randn(len(t))  # Weißes Rauschen
    temp_noisy = temp_clean + noise

    print(f"  Temperatursignal: {len(t)} Samples über {t[-1]:.0f} Sekunden")
    print(
        f"  SNR (Signal-to-Noise): {20 * np.log10(np.std(temp_clean) / np.std(noise)):.1f} dB"
    )

    # Verschiedene Filter anwenden
    window_sizes = [5, 15, 31]
    print("\n  Filter-Vergleich:")

    for window_size in window_sizes:
        # Einfacher gleitender Durchschnitt
        temp_ma_simple = moving_average_simple(temp_noisy, window_size)

        # Gewichteter gleitender Durchschnitt
        temp_ma_weighted = moving_average_weighted(temp_noisy, window_size)

        # Berechne Fehler (RMS) zum sauberen Signal
        # Anpassung der Längen für Vergleich
        clean_trimmed = temp_clean[window_size - 1 :]

        if len(temp_ma_simple) == len(clean_trimmed):
            rms_simple = np.sqrt(np.mean((temp_ma_simple - clean_trimmed) ** 2))
            rms_weighted = np.sqrt(np.mean((temp_ma_weighted - clean_trimmed) ** 2))

            print(
                f"    Fenster {window_size:2d}: RMS-Fehler einfach={rms_simple:.3f}, gewichtet={rms_weighted:.3f}"
            )

    # Exponentieller gleitender Durchschnitt
    alphas = [0.05, 0.1, 0.2]
    print("\n  Exponentieller Moving Average:")

    for alpha in alphas:
        temp_ema = exponential_moving_average(temp_noisy, alpha)
        rms_ema = np.sqrt(np.mean((temp_ema - temp_clean) ** 2))
        print(f"    Alpha {alpha:.2f}: RMS-Fehler = {rms_ema:.3f}")

    # 2.2 Frequency-Domain Filtering
    print("\n📊 2.2 Frequenzbereich-Filterung:")

    def low_pass_filter_fft(signal, fs, cutoff_freq):
        """Tiefpassfilter im Frequenzbereich"""
        # FFT des Signals
        signal_fft = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal), 1 / fs)

        # Filter-Maske erstellen
        filter_mask = np.abs(freqs) <= cutoff_freq

        # Filter anwenden
        filtered_fft = signal_fft * filter_mask

        # Zurück in Zeitbereich
        filtered_signal = np.real(np.fft.ifft(filtered_fft))

        return filtered_signal

    def band_pass_filter_fft(signal, fs, low_freq, high_freq):
        """Bandpassfilter im Frequenzbereich"""
        signal_fft = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal), 1 / fs)

        # Bandpass-Maske
        filter_mask = (np.abs(freqs) >= low_freq) & (np.abs(freqs) <= high_freq)

        filtered_fft = signal_fft * filter_mask
        filtered_signal = np.real(np.fft.ifft(filtered_fft))

        return filtered_signal

    # Simuliere Vibrationssignal mit mehreren Frequenzkomponenten
    fs = 1000  # Hz
    t_vib = np.linspace(0, 5, 5 * fs)

    # Signal mit verschiedenen Frequenzen
    signal_50hz = np.sin(2 * np.pi * 50 * t_vib)  # Maschinenfrequenz
    signal_150hz = 0.5 * np.sin(2 * np.pi * 150 * t_vib)  # 3. Harmonische
    signal_300hz = 0.3 * np.sin(2 * np.pi * 300 * t_vib)  # Lagerfrequenz
    high_freq_noise = 0.2 * np.sin(2 * np.pi * 800 * t_vib)  # Hochfrequentes Rauschen

    vibration_signal = signal_50hz + signal_150hz + signal_300hz + high_freq_noise
    vibration_signal += 0.1 * np.random.randn(len(t_vib))  # Rauschen

    print(f"  Vibrationssignal: {len(t_vib)} Samples @ {fs} Hz")
    print("  Frequenzkomponenten: 50, 150, 300, 800 Hz + Rauschen")

    # Verschiedene Filter testen
    # Tiefpass: Nur 50Hz und 150Hz durchlassen
    vib_lowpass = low_pass_filter_fft(vibration_signal, fs, 200)

    # Bandpass: Nur 150Hz Bereich
    vib_bandpass = band_pass_filter_fft(vibration_signal, fs, 100, 200)

    # Analyse der Filter-Effektivität
    def analyze_frequency_content(signal, fs, name):
        """Analysiere Frequenzinhalt eines Signals"""
        signal_fft = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal), 1 / fs)
        power_spectrum = np.abs(signal_fft) ** 2

        # Finde dominante Frequenzen (positive Frequenzen)
        positive_freqs = freqs[: len(freqs) // 2]
        positive_power = power_spectrum[: len(power_spectrum) // 2]

        # Top 3 Frequenzen
        top_indices = np.argsort(positive_power)[-3:][::-1]
        top_freqs = positive_freqs[top_indices]
        top_powers = positive_power[top_indices]

        print(f"    {name}:")
        for i, (freq, power) in enumerate(zip(top_freqs, top_powers, strict=False)):
            print(f"      #{i + 1}: {freq:.1f} Hz (Power: {power:.2e})")

    print("\n  Frequenzanalyse der gefilterten Signale:")
    analyze_frequency_content(vibration_signal, fs, "Original")
    analyze_frequency_content(vib_lowpass, fs, "Tiefpass (≤200Hz)")
    analyze_frequency_content(vib_bandpass, fs, "Bandpass (100-200Hz)")

    # 2.3 Adaptive Filterung
    print("\n📊 2.3 Adaptive Filterung:")

    def median_filter(signal, window_size):
        """Median-Filter für Impuls-Rauschunterdrückung"""
        filtered = np.zeros_like(signal)
        half_window = window_size // 2

        for i in range(len(signal)):
            start = max(0, i - half_window)
            end = min(len(signal), i + half_window + 1)
            filtered[i] = np.median(signal[start:end])

        return filtered

    def savitzky_golay_filter(signal, window_size, poly_order):
        """Vereinfachter Savitzky-Golay Filter"""
        # Für Demo-Zwecke: Lokale Polynomanpassung
        filtered = np.zeros_like(signal)
        half_window = window_size // 2

        for i in range(len(signal)):
            start = max(0, i - half_window)
            end = min(len(signal), i + half_window + 1)

            if end - start > poly_order:
                # Lokale x-Werte
                x_local = np.arange(start, end) - i
                y_local = signal[start:end]

                # Polynomanpassung
                poly_coeffs = np.polyfit(x_local, y_local, poly_order)
                filtered[i] = poly_coeffs[-1]  # Konstanter Term (Wert bei x=0)
            else:
                filtered[i] = signal[i]

        return filtered

    # Test mit Signal mit Impuls-Rauschen
    clean_signal = np.sin(0.1 * np.arange(200)) + 0.5 * np.sin(0.3 * np.arange(200))

    # Füge Impuls-Rauschen hinzu
    impulse_noise = np.zeros_like(clean_signal)
    impulse_positions = np.random.choice(len(clean_signal), 20, replace=False)
    impulse_noise[impulse_positions] = 10 * np.random.randn(20)

    noisy_signal = clean_signal + impulse_noise

    print(
        f"  Test-Signal: {len(clean_signal)} Samples mit {len(impulse_positions)} Impulsen"
    )

    # Verschiedene Filter vergleichen
    ma_filtered = moving_average_simple(noisy_signal, 5)
    median_filtered = median_filter(noisy_signal, 5)
    sg_filtered = savitzky_golay_filter(noisy_signal, 9, 2)

    # RMS-Fehler berechnen
    rms_noisy = np.sqrt(np.mean((noisy_signal - clean_signal) ** 2))
    rms_median = np.sqrt(np.mean((median_filtered - clean_signal) ** 2))
    rms_sg = np.sqrt(np.mean((sg_filtered - clean_signal) ** 2))

    print("\n  Filter-Performance (RMS-Fehler):")
    print(f"    Unbehandelt:        {rms_noisy:.3f}")
    print(
        f"    Median-Filter:      {rms_median:.3f} ({rms_noisy / rms_median:.1f}x besser)"
    )
    print(f"    Savitzky-Golay:     {rms_sg:.3f} ({rms_noisy / rms_sg:.1f}x besser)")

    duration = time.time() - start_time
    print(f"\n⚡ Signalverarbeitung in {duration:.3f} Sekunden")
    print("🔊 Verschiedene Filter sind für verschiedene Rauscharten optimal!")
    print()


def aufgabe_3_fourier_analysis():
    """Aufgabe 3: Fourier-Analyse für Frequenzdomäne"""
    print("🎯 AUFGABE 3: FOURIER-ANALYSE FÜR FREQUENZDOMÄNE")
    print("-" * 50)
    print("Ziel: Nutze FFT für Frequenzanalyse von Maschinensignalen")
    print("und Identifikation von Schwingungsmustern")
    print()

    start_time = time.time()

    # 3.1 Grundlegende FFT-Analyse
    print("📊 3.1 Grundlegende FFT-Analyse:")

    def analyze_spectrum(signal, fs, title="Signal"):
        """Analysiere Frequenzspektrum eines Signals"""
        n = len(signal)

        # FFT berechnen
        signal_fft = np.fft.fft(signal)
        freqs = np.fft.fftfreq(n, 1 / fs)

        # Power Spectral Density
        psd = np.abs(signal_fft) ** 2 / n

        # Nur positive Frequenzen (wegen Symmetrie)
        positive_freqs = freqs[: n // 2]
        positive_psd = psd[: n // 2]

        # Dominante Frequenzen finden
        peak_indices = np.argsort(positive_psd)[-5:][::-1]  # Top 5
        peak_freqs = positive_freqs[peak_indices]
        peak_powers = positive_psd[peak_indices]

        print(f"  {title}:")
        print(f"    Frequenzbereich: 0 - {fs / 2:.1f} Hz")
        print(f"    Frequenzauflösung: {fs / n:.2f} Hz")
        print("    Dominante Frequenzen:")

        for i, (freq, power) in enumerate(zip(peak_freqs, peak_powers, strict=False)):
            if power > np.max(positive_psd) * 0.01:  # Nur signifikante Peaks
                print(f"      #{i + 1}: {freq:.2f} Hz (Power: {power:.2e})")

        return positive_freqs, positive_psd

    # Simuliere Maschinensignal mit bekannten Frequenzen
    fs = 2048  # Sampling-Frequenz
    t = np.linspace(0, 10, 10 * fs)  # 10 Sekunden

    # Verschiedene Frequenzkomponenten
    main_frequency = 25.6  # Hauptspindelfrequenz
    harmonic_2 = 2 * main_frequency
    harmonic_3 = 3 * main_frequency
    bearing_freq = 127.3  # Lagerfrequenz

    # Zusammengesetztes Signal
    signal = (
        1.0 * np.sin(2 * np.pi * main_frequency * t)
        + 0.3 * np.sin(2 * np.pi * harmonic_2 * t)
        + 0.1 * np.sin(2 * np.pi * harmonic_3 * t)
        + 0.2 * np.sin(2 * np.pi * bearing_freq * t)
        + 0.05 * np.random.randn(len(t))
    )

    print(f"  Test-Signal: {len(t)} Samples @ {fs} Hz")
    print(
        f"  Erwartete Frequenzen: {main_frequency}, {harmonic_2:.1f}, {harmonic_3:.1f}, {bearing_freq:.1f} Hz"
    )

    freqs, psd = analyze_spectrum(signal, fs, "Maschinensignal")

    # 3.2 Fensterung für bessere Frequenzauflösung
    print("\n📊 3.2 Fensterung für FFT:")

    def windowed_fft(signal, fs, window_type="hann"):
        """FFT mit verschiedenen Fenstern"""
        n = len(signal)

        # Verschiedene Fenster
        windows = {
            "rectangular": np.ones(n),
            "hann": np.hanning(n),
            "hamming": np.hamming(n),
            "blackman": np.blackman(n),
        }

        if window_type in windows:
            window = windows[window_type]
        else:
            window = np.ones(n)

        # Windowing anwenden
        windowed_signal = signal * window

        # FFT berechnen
        signal_fft = np.fft.fft(windowed_signal)
        freqs = np.fft.fftfreq(n, 1 / fs)

        # Leistungsdichtespektrum (normalisiert)
        psd = np.abs(signal_fft) ** 2 / (np.sum(window**2))

        return freqs[: n // 2], psd[: n // 2]

    # Teste verschiedene Fenster
    window_types = ["rectangular", "hann", "hamming", "blackman"]

    print("  Fenster-Vergleich für Spektralanalyse:")

    for window_type in window_types:
        freqs_w, psd_w = windowed_fft(signal, fs, window_type)

        # Finde Peak um Hauptfrequenz
        freq_tolerance = 1.0  # Hz
        main_peak_mask = np.abs(freqs_w - main_frequency) < freq_tolerance

        if np.any(main_peak_mask):
            peak_power = np.max(psd_w[main_peak_mask])
            peak_freq = freqs_w[main_peak_mask][np.argmax(psd_w[main_peak_mask])]
            print(
                f"    {window_type:12s}: Peak @ {peak_freq:.2f} Hz, Power: {peak_power:.2e}"
            )

    # 3.3 Kurzzeitspektrum (STFT)
    print("\n📊 3.3 Kurzzeitspektrum (Short-Time FFT):")

    def short_time_fft(signal, fs, window_size, overlap=0.5):
        """Kurzzeitspektrum für zeitveränderliche Signale"""
        n = len(signal)
        step_size = int(window_size * (1 - overlap))

        # Anzahl Fenster
        n_windows = (n - window_size) // step_size + 1

        # Frequency bins
        freqs = np.fft.fftfreq(window_size, 1 / fs)[: window_size // 2]

        # Zeit-Achse für Fenster
        time_centers = np.arange(n_windows) * step_size / fs + window_size / (2 * fs)

        # Spektrogramm-Matrix
        spectrogram = np.zeros((len(freqs), n_windows))

        window = np.hanning(window_size)

        for i in range(n_windows):
            start_idx = i * step_size
            end_idx = start_idx + window_size

            if end_idx <= n:
                segment = signal[start_idx:end_idx] * window
                segment_fft = np.fft.fft(segment)
                spectrogram[:, i] = np.abs(segment_fft[: window_size // 2]) ** 2

        return time_centers, freqs, spectrogram

    # Simuliere zeitveränderliches Signal (Hochlauf einer Maschine)
    t_ramp = np.linspace(0, 20, 20 * fs)  # 20 Sekunden Hochlauf

    # Frequenz steigt linear von 10 Hz auf 100 Hz
    freq_ramp = 10 + (100 - 10) * t_ramp / 20
    phase = 2 * np.pi * np.cumsum(freq_ramp) / fs

    ramp_signal = np.sin(phase) + 0.1 * np.random.randn(len(t_ramp))

    print(f"  Hochlauf-Signal: {len(t_ramp)} Samples, {10} - {100} Hz über {20} s")

    # STFT berechnen
    window_size = 1024  # ~ 0.5s Fenster
    time_stft, freqs_stft, spectro = short_time_fft(ramp_signal, fs, window_size)

    print(f"  STFT: {len(time_stft)} Zeitfenster × {len(freqs_stft)} Frequenzbins")
    print(f"  Zeitauflösung: {time_stft[1] - time_stft[0]:.3f} s")
    print(f"  Frequenzauflösung: {freqs_stft[1] - freqs_stft[0]:.2f} Hz")

    # Analysiere Frequenzverlauf
    # Finde dominante Frequenz in jedem Zeitfenster
    dominant_freq_indices = np.argmax(spectro, axis=0)
    dominant_freqs = freqs_stft[dominant_freq_indices]

    # Erwartete vs. gemessene Frequenz
    expected_freqs = 10 + (100 - 10) * time_stft / 20
    freq_error = np.abs(dominant_freqs - expected_freqs)

    print("  Frequenzverfolgung:")
    print(f"    Mittlerer Fehler: {np.mean(freq_error):.2f} Hz")
    print(f"    Max. Fehler: {np.max(freq_error):.2f} Hz")

    # 3.4 Harmonische Analyse
    print("\n📊 3.4 Harmonische Analyse:")

    def harmonic_analysis(signal, fs, fundamental_freq, max_harmonics=10):
        """Analysiere harmonische Komponenten"""
        n = len(signal)
        signal_fft = np.fft.fft(signal)
        freqs = np.fft.fftfreq(n, 1 / fs)

        # Finde Harmonische
        harmonics_info = []

        for h in range(1, max_harmonics + 1):
            target_freq = h * fundamental_freq

            # Suche in Toleranzbereich um erwartete Frequenz
            tolerance = fundamental_freq * 0.1  # 10% Toleranz
            freq_mask = np.abs(freqs - target_freq) < tolerance

            if np.any(freq_mask):
                # Finde stärkste Komponente in diesem Bereich
                power_spectrum = np.abs(signal_fft) ** 2
                local_powers = power_spectrum[freq_mask]
                local_freqs = freqs[freq_mask]

                max_idx = np.argmax(local_powers)
                peak_freq = local_freqs[max_idx]
                peak_power = local_powers[max_idx]

                # Amplitude und Phase berechnen
                amplitude = 2 * np.abs(signal_fft[freq_mask][max_idx]) / n
                phase = np.angle(signal_fft[freq_mask][max_idx])

                harmonics_info.append(
                    {
                        "harmonic": h,
                        "frequency": peak_freq,
                        "amplitude": amplitude,
                        "phase": phase,
                        "power": peak_power,
                    }
                )

        return harmonics_info

    # Test mit künstlichem Signal mit bekannten Harmonischen
    fundamental = 30.0  # Hz
    t_harm = np.linspace(0, 5, 5 * fs)

    harmonics_signal = (
        2.0 * np.sin(2 * np.pi * fundamental * t_harm)  # 1. Harmonische
        + 1.0
        * np.sin(2 * np.pi * 2 * fundamental * t_harm + np.pi / 4)  # 2. Harmonische
        + 0.5
        * np.sin(2 * np.pi * 3 * fundamental * t_harm + np.pi / 2)  # 3. Harmonische
        + 0.2 * np.sin(2 * np.pi * 5 * fundamental * t_harm)
    )  # 5. Harmonische

    harmonics_signal += 0.1 * np.random.randn(len(t_harm))  # Rauschen

    print(f"  Harmonische Analyse für Grundfrequenz {fundamental} Hz:")

    harmonics_result = harmonic_analysis(harmonics_signal, fs, fundamental, 8)

    print("  Gefundene Harmonische:")
    for harm in harmonics_result:
        print(
            f"    {harm['harmonic']:2d}. Harm.: {harm['frequency']:6.2f} Hz, "
            f"Ampl.: {harm['amplitude']:5.3f}, Phase: {harm['phase']:6.2f} rad"
        )

    # 3.5 Power Spectral Density (PSD) Schätzung
    print("\n📊 3.5 Power Spectral Density Schätzung:")

    def welch_psd_estimate(signal, fs, window_size=None, overlap=0.5):
        """Welch-Methode für PSD-Schätzung"""
        if window_size is None:
            window_size = len(signal) // 8

        n = len(signal)
        step_size = int(window_size * (1 - overlap))
        n_windows = (n - window_size) // step_size + 1

        freqs = np.fft.fftfreq(window_size, 1 / fs)[: window_size // 2]
        psd_sum = np.zeros(len(freqs))

        window = np.hanning(window_size)
        window_norm = np.sum(window**2)

        for i in range(n_windows):
            start_idx = i * step_size
            end_idx = start_idx + window_size

            if end_idx <= n:
                segment = signal[start_idx:end_idx] * window
                segment_fft = np.fft.fft(segment)
                segment_psd = np.abs(segment_fft[: window_size // 2]) ** 2
                segment_psd /= fs * window_norm  # Normalisierung
                psd_sum += segment_psd

        psd_avg = psd_sum / n_windows
        return freqs, psd_avg

    # Vergleiche verschiedene PSD-Schätzmethoden
    test_signal = harmonics_signal  # Wiederverwende harmonisches Signal

    # Periodogramm (einfache FFT)
    n = len(test_signal)
    signal_fft = np.fft.fft(test_signal)
    freqs_periodo = np.fft.fftfreq(n, 1 / fs)[: n // 2]
    psd_periodo = np.abs(signal_fft[: n // 2]) ** 2 / (n * fs)

    # Welch-Methode
    freqs_welch, psd_welch = welch_psd_estimate(test_signal, fs)

    print("  PSD-Schätzung Vergleich:")

    # Vergleiche Frequenzauflösung
    print(
        f"    Periodogramm: {len(freqs_periodo)} Frequenzbins, Δf = {freqs_periodo[1]:.3f} Hz"
    )
    print(
        f"    Welch-Methode: {len(freqs_welch)} Frequenzbins, Δf = {freqs_welch[1]:.3f} Hz"
    )

    # Finde Peak-Power um Grundfrequenz
    for freqs_arr, psd_arr, method in [
        (freqs_periodo, psd_periodo, "Periodogramm"),
        (freqs_welch, psd_welch, "Welch"),
    ]:
        peak_mask = np.abs(freqs_arr - fundamental) < 2.0
        if np.any(peak_mask):
            peak_power = np.max(psd_arr[peak_mask])
            print(f"    {method}: Peak-Power @ {fundamental} Hz: {peak_power:.2e}")

    duration = time.time() - start_time
    print(f"\n⚡ Fourier-Analyse in {duration:.3f} Sekunden")
    print("📊 FFT ist essentiell für Maschinen-Diagnose und Qualitätskontrolle!")
    print()


def aufgabe_4_interpolation_fitting():
    """Aufgabe 4: Interpolation und Kurvenanpassung"""
    print("🎯 AUFGABE 4: INTERPOLATION UND KURVENANPASSUNG")
    print("-" * 50)
    print("Ziel: Implementiere Interpolations- und Fitting-Methoden")
    print("für Sensordaten und Kalibrierkurven")
    print()

    start_time = time.time()

    # 4.1 Verschiedene Interpolationsmethoden
    print("📊 4.1 Interpolationsmethoden:")

    def linear_interpolation(x_known, y_known, x_new):
        """Lineare Interpolation"""
        return np.interp(x_new, x_known, y_known)

    def polynomial_interpolation(x_known, y_known, x_new, degree):
        """Polynominterpolation"""
        coeffs = np.polyfit(x_known, y_known, degree)
        return np.polyval(coeffs, x_new)

    def spline_interpolation(x_known, y_known, x_new):
        """Vereinfachte kubische Spline-Interpolation"""
        # Für Demo: Stückweise kubische Polynome
        n = len(x_known)
        if n < 4:
            # Fallback auf Polynom niedrigerer Ordnung
            return polynomial_interpolation(x_known, y_known, x_new, min(n - 1, 3))

        # Erste Näherung: Lokale kubische Fits
        y_new = np.zeros_like(x_new)

        for i, x in enumerate(x_new):
            # Finde nächste Datenpunkte
            distances = np.abs(x_known - x)
            closest_indices = np.argsort(distances)[:4]  # 4 nächste Punkte

            x_local = x_known[closest_indices]
            y_local = y_known[closest_indices]

            # Lokale kubische Interpolation
            if len(np.unique(x_local)) >= 2:
                coeffs = np.polyfit(x_local, y_local, min(3, len(x_local) - 1))
                y_new[i] = np.polyval(coeffs, x)
            else:
                y_new[i] = np.mean(y_local)

        return y_new

    # Test mit Sensorkalibrierung (Temperatur vs. Widerstand)
    print("  Anwendung: Temperatursensor-Kalibrierung")

    # Kalibrierpunkte (Temperatur in °C, Widerstand in Ohm)
    temp_known = np.array([0, 25, 50, 75, 100, 125, 150])
    resistance_known = np.array([100.0, 109.7, 119.4, 129.1, 138.8, 148.5, 158.2])

    # Füge etwas Mess-Rauschen hinzu
    np.random.seed(42)
    resistance_known += 0.2 * np.random.randn(len(resistance_known))

    # Interpolation für feinere Temperaturauflösung
    temp_fine = np.linspace(0, 150, 301)  # 0.5°C Schritte

    print(
        f"    Kalibrierpunkte: {len(temp_known)} Messungen von {temp_known[0]} bis {temp_known[-1]}°C"
    )

    # Verschiedene Interpolationsmethoden testen
    resistance_linear = linear_interpolation(temp_known, resistance_known, temp_fine)
    resistance_poly3 = polynomial_interpolation(
        temp_known, resistance_known, temp_fine, 3
    )
    resistance_poly6 = polynomial_interpolation(
        temp_known, resistance_known, temp_fine, 6
    )
    resistance_spline = spline_interpolation(temp_known, resistance_known, temp_fine)

    # Validierung mit "wahrer" Funktion (PT100-ähnlich)
    def pt100_resistance(temp):
        """Näherung für PT100 Widerstand-Temperatur Beziehung"""
        R0 = 100.0  # Widerstand bei 0°C
        A = 3.9083e-3
        B = -5.775e-7
        return R0 * (1 + A * temp + B * temp**2)

    resistance_true = pt100_resistance(temp_fine)

    # RMS-Fehler berechnen
    rms_linear = np.sqrt(np.mean((resistance_linear - resistance_true) ** 2))
    rms_poly3 = np.sqrt(np.mean((resistance_poly3 - resistance_true) ** 2))
    rms_poly6 = np.sqrt(np.mean((resistance_poly6 - resistance_true) ** 2))
    rms_spline = np.sqrt(np.mean((resistance_spline - resistance_true) ** 2))

    print("\n  Interpolationsfehler (RMS vs. wahre Funktion):")
    print(f"    Linear:        {rms_linear:.4f} Ω")
    print(f"    Polynom Grad 3: {rms_poly3:.4f} Ω")
    print(f"    Polynom Grad 6: {rms_poly6:.4f} Ω")
    print(f"    Spline:        {rms_spline:.4f} Ω")

    # 4.2 Least-Squares Fitting
    print("\n📊 4.2 Least-Squares Kurvenanpassung:")

    def linear_least_squares(x, y):
        """Lineare Regression: y = ax + b"""
        n = len(x)
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        sum_xy = np.sum(x * y)
        sum_x2 = np.sum(x**2)

        # Normalgleichungen lösen
        a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
        b = (sum_y - a * sum_x) / n

        return a, b

    def polynomial_least_squares(x, y, degree):
        """Polynomiale Regression"""
        return np.polyfit(x, y, degree)

    def exponential_fit(x, y):
        """Exponentielles Fitting: y = a * exp(b*x)"""
        # Linearisierung: ln(y) = ln(a) + b*x
        ln_y = np.log(np.abs(y) + 1e-10)  # Vermeide log(0)
        b, ln_a = linear_least_squares(x, ln_y)
        a = np.exp(ln_a)
        return a, b

    # Simuliere Verschleißmessungen über Zeit
    np.random.seed(123)
    time_days = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300])

    # Wahre Verschleißfunktion (exponentiell)
    true_a, true_b = 0.1, 0.01
    wear_true = true_a * np.exp(true_b * time_days)

    # Messungen mit Rauschen
    wear_measured = wear_true + 0.02 * np.random.randn(len(time_days))

    print("  Anwendung: Werkzeugverschleiß-Modellierung")
    print(f"    Messdaten: {len(time_days)} Messungen über {time_days[-1]} Tage")

    # Verschiedene Fits versuchen
    # Linearer Fit
    a_lin, b_lin = linear_least_squares(time_days, wear_measured)
    wear_linear_fit = a_lin * time_days + b_lin

    # Polynomialer Fit (Grad 2)
    poly_coeffs = polynomial_least_squares(time_days, wear_measured, 2)
    wear_poly_fit = np.polyval(poly_coeffs, time_days)

    # Exponentieller Fit
    a_exp, b_exp = exponential_fit(time_days, wear_measured)
    wear_exp_fit = a_exp * np.exp(b_exp * time_days)

    # R² (Bestimmtheitsmaß) berechnen
    def r_squared(y_true, y_pred):
        ss_res = np.sum((y_true - y_pred) ** 2)
        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        return 1 - (ss_res / ss_tot)

    r2_linear = r_squared(wear_measured, wear_linear_fit)
    r2_poly = r_squared(wear_measured, wear_poly_fit)
    r2_exp = r_squared(wear_measured, wear_exp_fit)

    print("\n  Fitting-Qualität (R²):")
    print(f"    Linear:       {r2_linear:.4f}")
    print(f"    Quadratisch:  {r2_poly:.4f}")
    print(f"    Exponentiell: {r2_exp:.4f}")

    # Wahre Parameter vs. gefittete Parameter
    print("\n  Parameter-Vergleich (Exponentialfit):")
    print(f"    Wahre Parameter:     a = {true_a:.4f}, b = {true_b:.6f}")
    print(f"    Gefittete Parameter: a = {a_exp:.4f}, b = {b_exp:.6f}")
    print(
        f"    Relativer Fehler:    a: {abs(a_exp - true_a) / true_a * 100:.1f}%, b: {abs(b_exp - true_b) / true_b * 100:.1f}%"
    )

    # 4.3 Robuste Regression
    print("\n📊 4.3 Robuste Regression (Outlier-resistent):")

    def huber_loss_regression(x, y, delta=1.0, max_iterations=100):
        """Vereinfachte Huber-Loss Regression"""
        # Initialisierung mit linearer Regression
        a, b = linear_least_squares(x, y)

        for iteration in range(max_iterations):
            # Residuen berechnen
            y_pred = a * x + b
            residuals = y - y_pred

            # Huber-Gewichte
            abs_residuals = np.abs(residuals)
            weights = np.where(abs_residuals <= delta, 1.0, delta / abs_residuals)

            # Gewichtete Regression
            sum_w = np.sum(weights)
            sum_wx = np.sum(weights * x)
            sum_wy = np.sum(weights * y)
            sum_wxy = np.sum(weights * x * y)
            sum_wx2 = np.sum(weights * x**2)

            # Neue Parameter
            a_new = (sum_w * sum_wxy - sum_wx * sum_wy) / (sum_w * sum_wx2 - sum_wx**2)
            b_new = (sum_wy - a_new * sum_wx) / sum_w

            # Konvergenz prüfen
            if abs(a_new - a) < 1e-6 and abs(b_new - b) < 1e-6:
                break

            a, b = a_new, b_new

        return a, b

    # Test mit outlier-behafteten Daten
    # Basis-Daten (linearer Trend)
    x_robust = np.linspace(0, 10, 20)
    y_clean = 2.5 * x_robust + 1.0 + 0.3 * np.random.randn(len(x_robust))

    # Füge Outliers hinzu
    y_outliers = y_clean.copy()
    outlier_indices = [5, 12, 17]
    y_outliers[outlier_indices] += np.array([8, -6, 10])  # Starke Outliers

    print(f"  Test mit {len(outlier_indices)} Outliers in {len(x_robust)} Datenpunkten")

    # Verschiedene Regression-Methoden
    a_normal, b_normal = linear_least_squares(x_robust, y_outliers)
    a_huber, b_huber = huber_loss_regression(x_robust, y_outliers)

    # Wahre Parameter
    true_a_robust, true_b_robust = 2.5, 1.0

    print("  Regression-Vergleich:")
    print(f"    Wahre Parameter:    a = {true_a_robust:.2f}, b = {true_b_robust:.2f}")
    print(f"    Standard LS:        a = {a_normal:.2f}, b = {b_normal:.2f}")
    print(f"    Huber-Regression:   a = {a_huber:.2f}, b = {b_huber:.2f}")

    # Fehler zu wahren Parametern
    error_normal = np.sqrt(
        (a_normal - true_a_robust) ** 2 + (b_normal - true_b_robust) ** 2
    )
    error_huber = np.sqrt(
        (a_huber - true_a_robust) ** 2 + (b_huber - true_b_robust) ** 2
    )

    print("    Parameter-Fehler (Norm):")
    print(f"      Standard LS:      {error_normal:.3f}")
    print(
        f"      Huber-Regression: {error_huber:.3f} ({error_normal / error_huber:.1f}x besser)"
    )

    # 4.4 Spline-Glättung
    print("\n📊 4.4 Spline-Glättung für verrauschte Daten:")

    def smoothing_spline_simple(x, y, smoothing_factor=0.5):
        """Vereinfachte Spline-Glättung"""
        n = len(x)

        # Erstelle Glättungsmatrix (vereinfacht)
        # Kombination aus Datenfit und Glattheitsbedingung

        # Für Demo: Lokale Gewichtung mit Glättung
        y_smooth = np.zeros_like(y)

        for i in range(n):
            # Lokales Gewichtungsfenster
            distances = np.abs(x - x[i])
            max_distance = np.percentile(distances, 30)  # 30% nächste Punkte

            weights = np.exp(-((distances / max_distance) ** 2))
            weights[distances > max_distance] = 0

            # Gewichteter lokaler Fit
            if np.sum(weights) > 0:
                weights /= np.sum(weights)
                y_smooth[i] = np.sum(weights * y)
            else:
                y_smooth[i] = y[i]

        # Zusätzliche Glättung mit gleitendem Durchschnitt
        smoothing_window = max(3, int(n * smoothing_factor / 10))
        if smoothing_window % 2 == 0:
            smoothing_window += 1

        for _ in range(2):  # Mehrere Glättungsiterationen
            y_temp = np.zeros_like(y_smooth)
            half_window = smoothing_window // 2

            for i in range(n):
                start = max(0, i - half_window)
                end = min(n, i + half_window + 1)
                y_temp[i] = np.mean(y_smooth[start:end])

            y_smooth = y_temp

        return y_smooth

    # Test mit stark verrauschten Produktionsdaten
    x_noisy = np.linspace(0, 24, 100)  # 24 Stunden Produktion
    y_true_smooth = (
        100
        + 20 * np.sin(2 * np.pi * x_noisy / 12)
        + 10 * np.sin(2 * np.pi * x_noisy / 6)
    )  # Tägliche und 4h-Zyklen
    noise_level = 15
    y_noisy = y_true_smooth + noise_level * np.random.randn(len(x_noisy))

    print("  Anwendung: Produktions-Trendglättung")
    print(f"    Daten: {len(x_noisy)} Messungen über {x_noisy[-1]:.0f} Stunden")
    print(f"    SNR: {20 * np.log10(np.std(y_true_smooth) / noise_level):.1f} dB")

    # Verschiedene Glättungsgrade
    smoothing_factors = [0.1, 0.3, 0.5, 0.8]

    print("\n  Glättungs-Vergleich:")
    for factor in smoothing_factors:
        y_smoothed = smoothing_spline_simple(x_noisy, y_noisy, factor)

        # RMS-Fehler zum wahren Signal
        rms_error = np.sqrt(np.mean((y_smoothed - y_true_smooth) ** 2))
        rms_original = np.sqrt(np.mean((y_noisy - y_true_smooth) ** 2))

        improvement = rms_original / rms_error
        print(
            f"    Faktor {factor:.1f}: RMS-Fehler = {rms_error:.2f} ({improvement:.1f}x Verbesserung)"
        )

    duration = time.time() - start_time
    print(f"\n⚡ Interpolation und Fitting in {duration:.3f} Sekunden")
    print("📈 Richtige Interpolation ist kritisch für Sensor-Kalibrierung!")
    print()


def aufgabe_5_optimization():
    """Aufgabe 5: Optimierung und Root-Finding"""
    print("🎯 AUFGABE 5: OPTIMIERUNG UND ROOT-FINDING")
    print("-" * 45)
    print("Ziel: Implementiere numerische Optimierungsalgorithmen")
    print("für Produktionsparameter und Kalibrierprozesse")
    print()

    start_time = time.time()

    # 5.1 Root-Finding Algorithmen
    print("📊 5.1 Root-Finding (Nullstellensuche):")

    def bisection_method(func, a, b, tolerance=1e-6, max_iterations=100):
        """Bisektionsverfahren für Nullstellensuche"""
        if func(a) * func(b) > 0:
            raise ValueError("Funktion hat gleiches Vorzeichen an den Grenzen")

        for iteration in range(max_iterations):
            c = (a + b) / 2

            if abs(func(c)) < tolerance or abs(b - a) < tolerance:
                return c, iteration + 1

            if func(a) * func(c) < 0:
                b = c
            else:
                a = c

        return c, max_iterations

    def newton_raphson(func, func_derivative, x0, tolerance=1e-6, max_iterations=100):
        """Newton-Raphson Verfahren"""
        x = x0

        for iteration in range(max_iterations):
            fx = func(x)

            if abs(fx) < tolerance:
                return x, iteration + 1

            fpx = func_derivative(x)
            if abs(fpx) < 1e-12:
                raise ValueError("Ableitung zu klein (fast Null)")

            x_new = x - fx / fpx

            if abs(x_new - x) < tolerance:
                return x_new, iteration + 1

            x = x_new

        return x, max_iterations

    # Anwendung: Temperatur-Kalibrierung
    # Gegeben: Widerstandsmessung, gesucht: Temperatur
    print("  Anwendung: Temperatur aus Widerstandsmessung bestimmen")

    R_measured = 119.4  # Gemessener Widerstand in Ohm

    # PT100-Charakteristik: R(T) = R0 * (1 + A*T + B*T²)
    R0 = 100.0
    A = 3.9083e-3
    B = -5.775e-7

    def resistance_function(T):
        """R(T) - R_measured = 0"""
        return R0 * (1 + A * T + B * T**2) - R_measured

    def resistance_derivative(T):
        """Ableitung von R(T)"""
        return R0 * (A + 2 * B * T)

    print(f"    Gemessener Widerstand: {R_measured:.1f} Ω")
    print("    Gesucht: Temperatur T")

    # Bisektionsverfahren (robuster)
    T_bisection, iter_bisection = bisection_method(resistance_function, 0, 200)

    # Newton-Raphson (schneller, braucht Startwert)
    T_newton, iter_newton = newton_raphson(
        resistance_function, resistance_derivative, 50
    )

    # Analytische Lösung (quadratische Formel)
    # B*T² + A*T + (1 - R_measured/R0) = 0
    discriminant = A**2 - 4 * B * (1 - R_measured / R0)
    T_analytical = (-A + np.sqrt(discriminant)) / (2 * B)

    print("\n  Ergebnisse:")
    print(
        f"    Bisektionsverfahren: T = {T_bisection:.3f}°C ({iter_bisection} Iterationen)"
    )
    print(f"    Newton-Raphson:      T = {T_newton:.3f}°C ({iter_newton} Iterationen)")
    print(f"    Analytisch:          T = {T_analytical:.3f}°C")

    # Fehleranalyse
    print("  Abweichungen zur analytischen Lösung:")
    print(f"    Bisektionsverfahren: {abs(T_bisection - T_analytical):.6f}°C")
    print(f"    Newton-Raphson:      {abs(T_newton - T_analytical):.6f}°C")

    # 5.2 Eindimensionale Optimierung
    print("\n📊 5.2 Eindimensionale Optimierung:")

    def golden_section_search(func, a, b, tolerance=1e-6, max_iterations=100):
        """Golden Section Search für Minimum-Suche"""
        phi = (1 + np.sqrt(5)) / 2  # Goldener Schnitt
        resphi = 2 - phi

        # Erste Auswertungspunkte
        x1 = a + resphi * (b - a)
        x2 = b - resphi * (b - a)
        f1 = func(x1)
        f2 = func(x2)

        for iteration in range(max_iterations):
            if abs(b - a) < tolerance:
                return (a + b) / 2, func((a + b) / 2), iteration + 1

            if f1 < f2:
                b = x2
                x2 = x1
                f2 = f1
                x1 = a + resphi * (b - a)
                f1 = func(x1)
            else:
                a = x1
                x1 = x2
                f1 = f2
                x2 = b - resphi * (b - a)
                f2 = func(x2)

        return (a + b) / 2, func((a + b) / 2), max_iterations

    def parabolic_interpolation(func, x1, x2, x3, tolerance=1e-6, max_iterations=100):
        """Parabolische Interpolation für Optimierung"""
        for iteration in range(max_iterations):
            # Funktionswerte
            f1, f2, f3 = func(x1), func(x2), func(x3)

            # Parabolische Interpolation
            numerator = (x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1)
            denominator = 2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))

            if abs(denominator) < 1e-12:
                break

            x_new = x2 - numerator / denominator
            f_new = func(x_new)

            # Update der drei Punkte
            if x_new < x2:
                if f_new < f2:
                    x3, f3 = x2, f2
                    x2, f2 = x_new, f_new
                else:
                    x1, f1 = x_new, f_new
            else:
                if f_new < f2:
                    x1, f1 = x2, f2
                    x2, f2 = x_new, f_new
                else:
                    x3, f3 = x_new, f_new

            # Konvergenz prüfen
            if abs(x3 - x1) < tolerance:
                return x2, f2, iteration + 1

        return x2, func(x2), max_iterations

    # Anwendung: Optimale Schnittgeschwindigkeit
    print("  Anwendung: Optimale Schnittgeschwindigkeit für minimale Zykluszeit")

    def cycle_time_function(cutting_speed):
        """Zykluszeit als Funktion der Schnittgeschwindigkeit"""
        # Vereinfachtes Modell:
        # - Höhere Geschwindigkeit → weniger Schnittzeit
        # - Höhere Geschwindigkeit → mehr Werkzeugverschleiß → mehr Wechselzeit

        if cutting_speed <= 0:
            return float("inf")

        cutting_time = 100 / cutting_speed  # Grundschnittzeit
        tool_wear_factor = (cutting_speed / 100) ** 3  # Exponentieller Verschleiß
        tool_change_time = tool_wear_factor * 5  # Werkzeugwechselzeit

        return cutting_time + tool_change_time

    print("    Suchbereich: 10 - 200 m/min")

    # Golden Section Search
    opt_speed_golden, min_time_golden, iter_golden = golden_section_search(
        cycle_time_function, 10, 200
    )

    # Parabolische Interpolation (braucht 3 Startwerte)
    opt_speed_parabolic, min_time_parabolic, iter_parabolic = parabolic_interpolation(
        cycle_time_function, 50, 100, 150
    )

    print("\n  Optimierungsergebnisse:")
    print(
        f"    Golden Section:      v = {opt_speed_golden:.1f} m/min, "
        f"Zeit = {min_time_golden:.3f} min ({iter_golden} Iterationen)"
    )
    print(
        f"    Parabolisch:         v = {opt_speed_parabolic:.1f} m/min, "
        f"Zeit = {min_time_parabolic:.3f} min ({iter_parabolic} Iterationen)"
    )

    # 5.3 Mehrdimensionale Optimierung
    print("\n📊 5.3 Mehrdimensionale Optimierung:")

    def gradient_descent(
        func, grad_func, x0, learning_rate=0.01, tolerance=1e-6, max_iterations=1000
    ):
        """Gradient Descent für mehrdimensionale Optimierung"""
        x = np.array(x0, dtype=float)

        for iteration in range(max_iterations):
            grad = grad_func(x)

            if np.linalg.norm(grad) < tolerance:
                return x, func(x), iteration + 1

            x_new = x - learning_rate * grad

            if np.linalg.norm(x_new - x) < tolerance:
                return x_new, func(x_new), iteration + 1

            x = x_new

        return x, func(x), max_iterations

    def nelder_mead_simple(func, x0, tolerance=1e-6, max_iterations=1000):
        """Vereinfachte Nelder-Mead Optimierung"""
        n = len(x0)

        # Initialer Simplex (n+1 Punkte)
        simplex = [np.array(x0)]
        for i in range(n):
            point = np.array(x0)
            point[i] += 1.0  # Einfache Simplex-Erstellung
            simplex.append(point)

        # Funktionswerte
        f_values = [func(point) for point in simplex]

        for iteration in range(max_iterations):
            # Sortiere nach Funktionswerten
            indices = np.argsort(f_values)
            simplex = [simplex[i] for i in indices]
            f_values = [f_values[i] for i in indices]

            # Konvergenz prüfen
            if abs(f_values[-1] - f_values[0]) < tolerance:
                return simplex[0], f_values[0], iteration + 1

            # Schwerpunkt ohne schlechtesten Punkt
            centroid = np.mean(simplex[:-1], axis=0)

            # Spiegelung
            reflected = centroid + (centroid - simplex[-1])
            f_reflected = func(reflected)

            if f_values[0] <= f_reflected < f_values[-2]:
                # Akzeptiere Spiegelung
                simplex[-1] = reflected
                f_values[-1] = f_reflected
            elif f_reflected < f_values[0]:
                # Expansion
                expanded = centroid + 2 * (reflected - centroid)
                f_expanded = func(expanded)

                if f_expanded < f_reflected:
                    simplex[-1] = expanded
                    f_values[-1] = f_expanded
                else:
                    simplex[-1] = reflected
                    f_values[-1] = f_reflected
            else:
                # Kontraktion
                contracted = centroid + 0.5 * (simplex[-1] - centroid)
                f_contracted = func(contracted)

                if f_contracted < f_values[-1]:
                    simplex[-1] = contracted
                    f_values[-1] = f_contracted
                else:
                    # Schrumpfung
                    for i in range(1, len(simplex)):
                        simplex[i] = simplex[0] + 0.5 * (simplex[i] - simplex[0])
                        f_values[i] = func(simplex[i])

        return simplex[0], f_values[0], max_iterations

    # Anwendung: Optimierung von Produktionsparametern
    print("  Anwendung: Zwei-Parameter Produktionsoptimierung")

    def production_cost_function(params):
        """Produktionskosten als Funktion von [Geschwindigkeit, Vorschub]"""
        speed, feed = params

        if speed <= 0 or feed <= 0:
            return float("inf")

        # Vereinfachtes Modell
        cycle_time = 50 / (speed * feed)  # Weniger Zeit bei höheren Parametern
        tool_wear = 0.001 * speed**2 * feed  # Verschleiß steigt quadratisch
        quality_loss = 0.1 / (speed * feed) + 0.01 * speed * feed  # U-förmig

        return cycle_time + tool_wear + quality_loss

    def production_cost_gradient(params):
        """Gradient der Kostenfunktion"""
        speed, feed = params
        eps = 1e-6

        # Numerische Ableitung
        grad = np.zeros(2)
        grad[0] = (
            production_cost_function([speed + eps, feed])
            - production_cost_function([speed - eps, feed])
        ) / (2 * eps)
        grad[1] = (
            production_cost_function([speed, feed + eps])
            - production_cost_function([speed, feed - eps])
        ) / (2 * eps)

        return grad

    print("    Parameter: [Schnittgeschwindigkeit, Vorschub]")
    print("    Startwert: [100, 0.5]")

    # Gradient Descent
    opt_params_gd, min_cost_gd, iter_gd = gradient_descent(
        production_cost_function,
        production_cost_gradient,
        [100, 0.5],
        learning_rate=0.1,
    )

    # Nelder-Mead
    opt_params_nm, min_cost_nm, iter_nm = nelder_mead_simple(
        production_cost_function, [100, 0.5]
    )

    print("\n  Optimierungsergebnisse:")
    print(
        f"    Gradient Descent: [v={opt_params_gd[0]:.1f}, f={opt_params_gd[1]:.3f}], "
        f"Kosten={min_cost_gd:.4f} ({iter_gd} Iterationen)"
    )
    print(
        f"    Nelder-Mead:      [v={opt_params_nm[0]:.1f}, f={opt_params_nm[1]:.3f}], "
        f"Kosten={min_cost_nm:.4f} ({iter_nm} Iterationen)"
    )

    # 5.4 Constraint Optimization
    print("\n📊 5.4 Optimierung mit Nebenbedingungen:")

    def penalty_method_optimization(
        func, constraints, x0, penalty_factor=10, tolerance=1e-6, max_iterations=100
    ):
        """Penalty-Methode für constrained optimization"""

        def penalty_function(x):
            """Zielfunktion + Penalty für Constraint-Verletzungen"""
            f_val = func(x)
            penalty = 0

            for constraint in constraints:
                violation = max(0, constraint(x))  # Nur positive Verletzungen
                penalty += penalty_factor * violation**2

            return f_val + penalty

        # Verwende Nelder-Mead für penalty function
        return nelder_mead_simple(penalty_function, x0, tolerance, max_iterations)

    # Anwendung: Produktionsoptimierung mit Beschränkungen
    print("  Anwendung: Produktionsoptimierung mit Maschinenbeschränkungen")

    def constrained_production_function(params):
        """Zu minimierende Produktionszeit"""
        speed, feed = params
        return 100 / (speed * feed) if speed > 0 and feed > 0 else float("inf")

    # Constraints: Maschinenspezifikationen
    def speed_constraint(params):
        """Geschwindigkeit darf 150 nicht überschreiten"""
        return params[0] - 150

    def feed_constraint(params):
        """Vorschub darf 1.0 nicht überschreiten"""
        return params[1] - 1.0

    def power_constraint(params):
        """Leistungsbegrenzung: speed * feed² ≤ 50"""
        return params[0] * params[1] ** 2 - 50

    constraints = [speed_constraint, feed_constraint, power_constraint]

    print("    Constraints:")
    print("      Geschwindigkeit ≤ 150")
    print("      Vorschub ≤ 1.0")
    print("      Leistung: v × f² ≤ 50")

    # Optimierung mit Constraints
    opt_params_constrained, min_time_constrained, iter_constrained = (
        penalty_method_optimization(
            constrained_production_function, constraints, [100, 0.5]
        )
    )

    # Uneingeschränkte Optimierung zum Vergleich
    opt_params_unconstrained, min_time_unconstrained, iter_unconstrained = (
        nelder_mead_simple(constrained_production_function, [100, 0.5])
    )

    print("\n  Vergleich eingeschränkt vs. uneingeschränkt:")
    print(
        f"    Uneingeschränkt: [v={opt_params_unconstrained[0]:.1f}, f={opt_params_unconstrained[1]:.3f}], "
        f"Zeit={min_time_unconstrained:.4f}"
    )
    print(
        f"    Eingeschränkt:   [v={opt_params_constrained[0]:.1f}, f={opt_params_constrained[1]:.3f}], "
        f"Zeit={min_time_constrained:.4f}"
    )

    # Prüfe Constraint-Erfüllung
    print("  Constraint-Erfüllung (eingeschränkte Lösung):")
    for i, constraint in enumerate(constraints):
        violation = max(0, constraint(opt_params_constrained))
        status = "✓" if violation < 1e-6 else f"✗ ({violation:.3f})"
        print(f"    Constraint {i + 1}: {status}")

    duration = time.time() - start_time
    print(f"\n⚡ Optimierung in {duration:.3f} Sekunden")
    print("🎯 Numerische Optimierung ist essentiell für Produktionseffizienz!")
    print()


if __name__ == "__main__":
    main()
