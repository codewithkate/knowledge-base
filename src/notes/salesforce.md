---
title: "No-Code Solutions for Embedding Tableau in Salesforce"
date: 2024-11-12
summary: "A tutorial on Tableau Lightning Web Components for desktop and mobile."
tags: ["notes", "UI/UX", "system design"]
---

## What are Salesforce Lightning Apps?

Salesforce is an app-based platform that has several no-Code solutions for adding web components to its interface. This works similar to web objects on a Tableau Dashboard.

There are two kinds of Salesforce apps: Classic and Lightning. Using apps in Lightning Experience allows your users to access content that is relevant to them through the **App Launcher**.

![[sf-applauncher.png]]

>[!Note] 
>Your profile determines which apps you can view and build. For this tutorial, you will need an admin access in Salesforce and Tableau Cloud.

## Create a New Lightning App 

1. Go to your Salesforce Site. Click the gear icon (⚙️) in the top right header to navigate to **Setup**. 
2. Use Quick Find to search for **App Manager** under Apps.

![[sf-appmanager.png]]

3. Create a New Lightning App. 
4. Enter a descriptive name for the team or department and add any custom branding. 
5. Keep default app options, utility, and navigation items, unless you know the items you want to include as tabs in your app.
7. Choose the user profiles that can access the app.
8. Finally, go to the app through the App Launcher. Continue reading for how to add Tableau components to this app.

## Connect Tableau Cloud and Salesforce

Tableau has detailed step-by-step instructions to [configure Tableau Lightning Web Components and Single Sign-On (SSO) with token authentication](https://help.tableau.com/current/server/en-us/lwc_seamless_auth.htm).

>[!Note]
>Connections between Salesforce and Tableau Cloud Dev Sites have not worked in the past. It is recommended that you use active Tableau Cloud and Salesforce instances or Partner site credentials.

## Personalize App Home Page

We can create a new view to add to our home page. For this example, we will be embedding a Tableau Dashboard.

1. Go to Setup and search for **Lightning App Builder** from Quick Find. 
2. Click New to create a Home Page. 

![[sf-appbuilder.png]] 

3. Search for Tableau in the Components Panel.
	- **Tableau View**: embed a tableau dashboard or worksheet. (**choose this one**) 
	- **Tableau Pulse**: web component for pulse metrics.
4. Click and drag the **Tableau View Component** onto the main canvas. 
5. Copy/Paste the **URL** from Tableau cloud to your Tableau dashboard and the **Site ID** for your organization's Tableau Site.
6. Save the page and go to **Activation**.
7. Assign the page as the **home page** for select apps.

If the activation was successful, then go back to your app. We will need to add the home page to your navigation tabs.

1. Click the pencil (✏️) icon to the right of the App name. 
2. Add more items and search for Home.

You should see something like this:

![[sf-tableaudashboard.png]]

Continue reading to learn how to make mobile-friendly pages.

## Create a Mobile App Page for Pulse

You can't access Desktop views from the Mobile App. You must create a phone layout. 

1. Within Lightning App Builder, create a new page. 
2. Name it Tableau Pulse with a One Region layout.

You should see a Phone layout selected above the canvas:

![[sf-phonelayout.png]]

3. Search for Tableau Pulse component and drag it onto the canvas.
4. Open Tableau Pulse and paste the full URL (including your site name).
5. Open Connected Apps in Tableau Cloud Settings. Find the Salesforce connection (created earlier) and Copy Site ID to paste into the App Setup.

Now, you can move onto adjusting the Activation settings.

1. Page Settings: Choose a display name, icon, and manage access.
2. Lightning Experience: Add the page to multiple Lightning Apps.
3. Mobile Navigation: Add and reorder pages available in the Salesforce App.

Save and get ready to preview the page in the Salesforce Mobile App.

## Preview Pulse in the Salesforce Mobile App

After downloading the Salesforce App, go to your device settings. You will need to **Allow Cross-Website Tracking**.

![[sf-devicesettings.png]]

Open the Salesforce App and go to the **App Launcher** on the Menu page. 

Find **Mobile Only** and you should be able to view your Tableau Pulse app from the navigation menu. 

![[sf-pulsemobile.png]]

## Wrap-up

Having followed these steps, you are all set to customize Salesforce Desktop and Mobile!

## Additional Resources

- [Learning Module | Lightning App Builder](https://trailhead.salesforce.com/content/learn/modules/lightning_app_builder)
- [Learning Module | Lightning Experience Rollout](https://trailhead.salesforce.com/content/learn/modules/lex_migration_rollout)
- [Help Article | Extend Salesforce with Clicks, Not Code](https://help.salesforce.com/s/articleView?id=platform.extend_click_intro.htm&language=en_US&type=5)
- [Help Article | Configure Tableau and SSO](https://help.tableau.com/current/server/en-us/lwc_seamless_auth.htm)
- [Watch Demo | Build a Mobile App Page](https://admin.salesforce.com/blog/2019/build-a-mobile-app-page)
