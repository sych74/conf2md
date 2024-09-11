---
draft: false
title: "WHMCS Billing System"
aliases: "/whmcs-billing/"
seoindex: "index, follow"
seotitle: "WHMCS Billing System"
seokeywords: "whmcs, whmcs billing, whmcs billing system, whmcs billing paas, whmcs credit card, whmcs paypal, whmcs auto-refill"
seodesc: "This detailed manual describes how to upgrade and refill PaaS account via WHMCS billing system."
menu: 
    docs:
        title: "WHMCS Billing System"
        url: "/whmcs-billing/"
        weight: 40
        parent: "billing-systems"
        identifier: "whmcs-billing.md"
---

# Billing via WHMCS

This detailed manual describes how to upgrade and refill PaaS account via WHMCS billing system:

* [Upgrade](#trial-account-upgrade-to-billing)
* [Refill](#refilling-account-via-whmcs)


## Trial Account Upgrade to Billing

1\. Click the **Upgrade trial account** button and choose the same-named option from the drop-down menu.

![upgrade trial account](upgrade-trial.png)

2\. Within the opened form, fill in the required fields and accept the *Terms of Service*  agreement.

![upgrade account form](upgrade-to-paid.png)

{{%tip%}}**Note:** 

* <u>*if you have the WHMCS account*</u>, registered for the same email as the PaaS account, they will be connected automatically
* <u>*if you do not have the WHMCS account*</u>, the platform will automatically generate it for you (whilst you'll receive the appropriate email with WHMCS admin panel access URL and your credentials){{%/tip%}}

Click **Continue**.

3\. Next, select the preferable payment method and specify the required payment sum with a slider.

![trial to paid conversion](trial-to-paid-conversion.png)

{{%tip%}}**Notes:** 

* consider that *VAT* (tax amount) is not displayed in the dashboard UI
* some hosting providers propose the alternative payment methods, given in addition to the default ones. In this case, you'll be offered to contact the hosting provider in order to use some other ways of funding{{%/tip%}}

Click **Submit** and confirm your choice.

### Card Payment Method

Specify your card details and click **Continue**.

![WHMCS payment](credir-card-method.png)

Next, within the opened **Purchase Authentication** window, type the password for authentication.

### PayPal Payment Method

* <u>*with PayPal account*</u>

Click the **Log In** button and enter your PayPal account credentials (email and password) to make a purchase.

![PayPal log in](paypal-log.png)

![PayPal log in form](log-in-paypal.png)

Once your PaaS account is successfully converted to billing, you'll receive the appropriate notifications on its upgrade and balance refilling via email. Also, similar messages will appear at the dashboard.

{{%tip%}}**Note:** If you would like to use the balance auto-refill option, don't forget to tick the "I'd like to use PayPal for future payments to *{hoster's name}*" line as it is shown below:

![PayPal auto-refill](paypal-autorefill.png){{%/tip%}}

* <u>*without PayPal account*</u>

If you don't have a PayPal account yet, just click the **Buy as a guest** button. Specify your billing information in the opened window.

![PayPal guest info](paypal-guest.png)

Click **Continue** and provide your debit/credit card details in the appeared window.

![PayPal guest](guest-card-number.png)

Once your PaaS account is successfully converted to billing, you'll receive the appropriate notifications on its upgrade and balance refilling via email. Also, similar messages will appear at the dashboard.

{{%tip%}}**Note:** Use of the auto-refill option is unavailable when recharging balance as a guest in PayPal (i.e. the appropriate option won't be enabled even if being ticked).{{%/tip%}}


## Refilling Account via WHMCS

1\. In order to replenish your account, select the **Balance > Refill balance** option at the top of dashboard.

![refill balance](credit-debit-refill.png)

State the required sum using the appropriate slider, choose the prefered payment method and click on **Submit Payment**.

{{%tip%}}**Note:** The *VAT* (tax amount) will be shown only when proceeding the payment in the order.{{%/tip%}}

### Card Payment Method

Specify your card details and click **Submit Payment**.

![card refill](card-refill.png)

{{%tip%}}**Note:** In case you've already refilled your account with this card, you won't need to enter card details again - just confirm the refilling.{{%/tip%}}

### PayPal Payment Method

Log in to your PayPal account and complete the purchase.

![PayPal refill](paypal-refill.png)

After the replenishment completion, you'll receive an email with information about your account refilling. Also, the appropriate message will appear at the dashboard.

2\. Additionally, you are able to configure the auto-refill option, if needed. For that choose the **Configure auto-refill** item in the **Balance** drop-down menu.

![configure auto-refill](configure-autorefill.png)

Within the opened tab state the sum you would like to put on your account and choose the refilling frequency:

* *weekly* (every Monday)
* *monthly* (1st of each month)
* when *balance less than* the stated sum (up to your choice)

![auto-refill Visa](autorefill-visa.png)

**Confirm** your choice.

{{%tip%}}**Note:** As WHMCS doesn't truly supports auto-recharge feature, the platform **automatically** creates order (threshold or monthly trigger based) for a particular recharge card. So the payment can be made in two ways:

* *automatically* - if you have a positive WHMCS balance that is greater or equals to order amount
* *manually* - the confirmation email is automatically sent to you before completing each order{{%/tip%}}

3\. If you want to switch off the **Auto refill** option, click the appropriate link to disable it.

![switch off auto-refill](switch-off-autorefill.png)

4\. After clicking the **Payment methods** option from the **Balance** drop-down menu, you can select your default payment method which will be used automatically while refilling.

5\. Click **View invoices** to open WHMCS admin panel with your Billing history which includes all financial documents issued for your Account (i.e. Invoices, Orders, Payments, and Adjustments).

![invoice](invoice.png)

6\. Click **Billing history** to view the data about consumed resources on your account and the appropriate charges by the platform.


## What's next?

* [Billing Systems Overview](/billing-system/)
* [PBA Billing System](/oba-billing-system/)
* [PBAS Billing System](/obas/)
* [Hosters Info](/paas-hosting-providers/)
* [Hosters Pricing](/pricing-pages/)